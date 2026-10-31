import { describe, it, expect } from 'vitest';
import { BASE_BANK, SUBJECTS, createExam, grade, emptyStore, submitExam, answerExam, remainingSeconds, validateQuestion, fingerprint, importQuestions, parseCsv, restoreStore, startPractice, checkPractice, nextPractice } from '../src/model';
import { readFileSync } from 'node:fs';

describe('은행 구조·권리·중복·등록 수', () => {
 it('220개 자체 제작, 과목 50/50/50/50/20, 미확인 출제 회차 없음', () => {
  expect(BASE_BANK).toHaveLength(220);
  expect(SUBJECTS.map(s => BASE_BANK.filter(q=>q.subject===s).length)).toEqual([50,50,50,50,20]);
  expect(new Set(BASE_BANK.map(q=>q.id)).size).toBe(220);
  expect(new Set(BASE_BANK.map(fingerprint)).size).toBe(220);
  for(const q of BASE_BANK) { expect(validateQuestion(q)).toEqual(q); expect(q.year).toBeNull();expect(q.session).toBeNull();expect(q.type).toBe('original'); }
  expect(new Set(BASE_BANK.filter(q=>q.family).map(q=>q.family)).size).toBe(20);
 });
 it('보기 순서를 바꾼 중복도 제외, 잘못된 입력은 원자적으로 거부',()=>{
  expect(importQuestions([{...BASE_BANK[0],id:'DIFFERENT', choices:[...BASE_BANK[0].choices].reverse()}],BASE_BANK).duplicates).toBe(1);
  expect(()=>importQuestions([{...BASE_BANK[0],id:'NEW',question:'새 문항'},{}],BASE_BANK)).toThrow('2번 문항');
  expect(importQuestions([{...BASE_BANK[0],id:'NEW',question:'새 문항'}],BASE_BANK).added[0].verificationStatus).toBe('pending');
 });
 it('CSV·JSON 양식이 현재 자격증 스키마에 부합',()=>{
  for(const q of parseCsv(readFileSync('public/templates/questions.csv','utf8'))) expect(validateQuestion(q).subject).toBe(SUBJECTS[0]);
  expect(validateQuestion(JSON.parse(readFileSync('public/templates/questions.json','utf8'))[0]).version).toBe('main');
 });
});
// Algebraic inverses / conservation identities, separate from the generating expressions.
// Compare the displayed rounded choice, not just the hidden result metadata.
for(const q of BASE_BANK.filter(q=>q.calculation)) {
 it(`독립 역산·보기 유일성 ${q.id} ${q.calculation!.kind}`,()=>{
  const {values:v,kind}=q.calculation!; const text=q.choices[q.answer-1]; const r=Number(text.split(' ')[0]);
  const near=(actual:number, expected:number, scale=1)=>expect(Math.abs(actual-expected)).toBeLessThanOrEqual(.000501*Math.abs(scale)+1e-8);
  switch(kind) {
   case 'mass-load':near(r*1000/v[0],v[1],1000/v[0]);break;
   case 'concentration':near(r*v[1],v[0],v[1]);break;
   case 'mix':near((r-v[1])*v[0],(v[3]-r)*v[2],v[0]+v[2]);break;
   case 'removal':near(v[0]*(1-r/100),v[1],v[0]/100);break;
   case 'half-life':near(r*2**v[1],v[0],2**v[1]);break;
   case 'daily-water':near(r/v[0]*1000,v[1],1000/v[0]);break;
   case 'storage':case 'tank-volume':near(r/v[0]*24,v[1],24/v[0]);break;
   case 'pipe-flow':near(r/v[0],v[1],1/v[0]);break;
   case 'peak':near(r/v[0],v[1],1/v[0]);break;
   case 'overflow':near(r*v[1],v[0],v[1]);break;
   case 'fm':near(r*v[1]*v[2]/1000,v[0],v[1]*v[2]/1000);break;
   case 'dose':near(r*1e6,v[0]*1000*v[1],1e6);break;
   case 'srt':near(r*v[2],v[0]*v[1]/1000,v[2]);break;
   case 'series':near(r/(1-v[1]/100)/(1-v[2]/100),v[0],1/(1-v[1]/100)/(1-v[2]/100));break;
   case 'dilution':near(r*v[0],v[2]*v[1],v[0]);break;
   case 'calibration':near(v[0]*r+v[1],v[2],v[0]);break;
   case 'recovery':near(v[0]+r*v[1]/100,v[2],v[1]/100);break;
   case 'bod':near(r*v[2]+v[1],v[0],v[2]);break;
   case 'gravimetric':near(r*v[2]/1e6+v[0],v[1],v[2]/1e6);break;
   default:throw new Error('미검증 계산 유형');
  }
  const nums=q.choices.map(c=>Number(c.split(' ')[0]));
  expect(new Set(nums).size).toBe(4);
  expect(Math.abs(r-q.calculation!.result)).toBeLessThanOrEqual(.000501);
  expect(q.explanation).not.toContain('undefined');
 });
}
describe('5과목·100문항·150분·평균·과락',()=>{
 it('검수 완료만 추출, 고유 ID·과목별 20·절대 종료 시각',()=>{
  const e=createExam(BASE_BANK,'main',1000);expect(e.questions).toHaveLength(100);
  expect(e.deadline).toBe(9001000);expect(new Set(e.questions.map(q=>q.id)).size).toBe(100);
  for(const s of SUBJECTS)expect(e.questions.filter(q=>q.subject===s)).toHaveLength(20);
  expect(()=>createExam(BASE_BANK.filter(q=>q.subject!==SUBJECTS[4]),'main')).toThrow();
 });
 function examWith(counts:number[]) {
  const e=createExam(BASE_BANK,'main',0);
  SUBJECTS.forEach((s,i)=>e.questions.filter(q=>q.subject===s).slice(0,counts[i]).forEach(q=>e.answers[q.id]=q.answer)); return e;
 }
 it.each([[12,12,12,12,12,true],[11,12,12,12,12,false],[20,20,20,20,7,false],[20,20,20,20,8,true]])('합격 경계 %j',(...args)=>{
  const passed=args.pop();expect(grade(examWith(args as number[])).passed).toBe(passed);
 });
 it('평균 80점이어도 한 과목 35점이면 불합격·미응답은 오답',()=>{
  const g=grade(examWith([20,20,20,13,7]));expect(g.score).toBe(80);expect(g.passed).toBe(false);expect(g.unanswered).toBe(20);
 });
 it('만료 입력 거부·자동 제출·중복 제출 방지',()=>{
  const e=createExam(BASE_BANK,'main',100);const s={...emptyStore(),exam:e};
  const done=answerExam(s,e.questions[0].id,1,e.deadline);expect(done.exam).toBeNull();expect(done.results[0].answers).toEqual({});
  expect(submitExam(done)).toBe(done);expect(remainingSeconds(e.deadline,e.deadline+1)).toBe(0);
 });
 it('복원 시간·과목 수 검사·손상 거부',()=>{
  const s={...emptyStore(),exam:createExam(BASE_BANK,'main')};expect(restoreStore(JSON.stringify(s))).toEqual(s);
  expect(()=>restoreStore('{broken')).toThrow();s.exam.deadline+=1;expect(()=>restoreStore(JSON.stringify(s))).toThrow();
 });
 it('랜덤 순회·즉시 채점 1회·정답 재학습으로 오답 해제',()=>{
  let s=emptyStore();s.practice=startPractice(BASE_BANK,'main',SUBJECTS[4]);const seen=new Set<string>();
  for(let i=0;i<20;i++){expect(seen.has(s.practice!.currentId)).toBe(false);seen.add(s.practice!.currentId);s.practice=nextPractice(s.practice!,BASE_BANK);}
  const q=BASE_BANK.find(q=>q.id===s.practice!.currentId)!;s.wrongIds=[q.id];s.practice!.selected=q.answer;
  s=checkPractice(s,BASE_BANK);expect(s.wrongIds).toEqual([]);expect(checkPractice(s,BASE_BANK)).toBe(s);expect(s.attempts).toHaveLength(1);
 });
});
