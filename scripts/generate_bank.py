"""Deterministic authored practice material; not past examination questions.
20 numeric families × 10 + 26 numeric families × 30 + 20 concepts = 1000.
AI general knowledge, no external source was successfully read.
"""
import json,csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SUBJECTS=['수질오염개론','상하수도계획','수질오염방지기술','수질오염공정시험기준','수질환경관계법규']
BANK=[]
def add(subject,topic,stem,explanation,choices,answer,family=None,kind=None,values=None,result=None,unit=None):
 q=dict(id=f'W-{len(BANK)+1:04}',subject=SUBJECTS[subject],topic=topic,question=stem,choices=choices,answer=answer,explanation=explanation,difficulty='중',year=None,session=None,type='original',sourceUrl='https://github.com/YunSangYeong/Engineer-Water-Environmental-Pollution-Control-CBT',verificationStatus='reviewed',reviewNote='AI 일반 지식으로 자체 작성. 조건·단위·정답 유일성·해설을 내부 검토. 계산은 별도 역산 검사. 공식 출제기준 대조·외부 전문가 검수 미완료. 출처 링크는 작성 위치이며 외부 정답 근거가 아님.',version='main',rights='자체 제작 자료 CC BY 4.0 · 수질환경기사 CBT contributors 표시 · 변경 표시')
 if family:q['family']=family;q['calculation']=dict(kind=kind,values=values,result=result,unit=unit,precision=3)
 BANK.append(q)
def numeric(subject,topic,kind,stem,formula,result,values,unit,j):
 # Values selected to keep all alternatives distinct; precision explicit in stem.
 answers=[result,result*1.5,result*2,result*.5]
 offset=j%4;answers=answers[offset:]+answers[:offset]
 def fmt(x):return f'{x:.3f}'.rstrip('0').rstrip('.')
 add(subject,topic,stem+' 결과는 소수 셋째 자리까지 반올림한다.',formula+f' 따라서 {fmt(result)} {unit}이다. 보기 단위는 모두 동일하다.',[fmt(x)+' '+unit for x in answers],answers.index(result)+1,kind,kind,values,result,unit)
for j in range(10):
 q=1000+200*j;c=20+2*j
 numeric(0,'오염부하량','mass-load',f'유량 {q} m³/일, 농도 {c} mg/L인 하천의 물질 부하량(kg/일)은?',f'1 m³=1,000 L, 1 kg=1,000,000 mg. 부하량=Q×C/1,000={q}×{c}/1,000.',q*c/1000,[q,c],'kg/일',j)
 m=50+10*j;v=2+j
 numeric(0,'질량농도','concentration',f'물 {v} L에 용질 {m} mg을 녹였다. 부피 변화가 없을 때 농도(mg/L)는?',f'농도=질량/부피={m}/{v}.',m/v,[m,v],'mg/L',j)
 q1=10+j;q2=20+j;c1=10;c2=40
 numeric(0,'완전혼합','mix',f'{c1} mg/L 물 {q1} m³/일과 {c2} mg/L 물 {q2} m³/일이 반응 없이 완전 혼합된다. 혼합 농도는?',f'질량보존으로 혼합 농도=(Q₁C₁+Q₂C₂)/(Q₁+Q₂)=({q1}×{c1}+{q2}×{c2})/({q1}+{q2}).',(q1*c1+q2*c2)/(q1+q2),[q1,c1,q2,c2],'mg/L',j)
 ci=100+10*j;co=20+j
 numeric(0,'제거율','removal',f'유입 농도 {ci} mg/L, 유출 농도 {co} mg/L이다. 유량 변화가 없을 때 제거율(%)은?',f'제거율=(유입−유출)/유입×100=({ci}−{co})/{ci}×100.',(ci-co)/ci*100,[ci,co],'%',j)
 initial=80+8*j;halves=2+j%3
 numeric(0,'1차 반감기','half-life',f'반감기가 일정한 물질의 초기 농도는 {initial} mg/L이다. 반감기의 {halves}배 시간이 경과한 농도는?',f'반감기마다 절반으로 감소하므로 C=C₀×(1/2)ⁿ={initial}/2^{halves}.',initial/(2**halves),[initial,halves],'mg/L',j)
 population=10000+1000*j;use=200+10*j
 numeric(1,'급수량','daily-water',f'급수 인구 {population}명, 1인 1일 평균 급수량 {use} L/인·일이다. 손실을 무시한 일평균 급수량은?',f'일평균 급수량=인구×원단위/1,000={population}×{use}/1,000.',population*use/1000,[population,use],'m³/일',j)
 daily=2400+240*j;hours=4+j
 numeric(1,'저류용량','storage',f'균일한 물 사용량은 {daily} m³/일이다. {hours}시간 사용량을 저장할 순수 저류용량은?',f'시간당 사용량=Q/24이므로 V=Q×t/24={daily}×{hours}/24.',daily*hours/24,[daily,hours],'m³',j)
 area=0.5+j*.1;velocity=1+j*.1
 numeric(1,'관로 유량','pipe-flow',f'만관 흐름의 단면적 {area:.1f} m², 평균 유속 {velocity:.1f} m/s이다. 유량은?',f'연속식 Q=A×v={area:.1f}×{velocity:.1f}.',area*velocity,[area,velocity],'m³/s',j)
 flow=1000+100*j;retention=2+j*.2
 numeric(1,'체류시간 설계','tank-volume',f'일정 유량 {flow} m³/일을 {retention:.1f}시간 체류시키는 이상적 탱크의 용량은?',f'V=Q×t/24={flow}×{retention:.1f}/24.',flow*retention/24,[flow,retention],'m³',j)
 base=2000+200*j;factor=1.5+j*.1
 numeric(1,'첨두계수','peak',f'평균 유량 {base} m³/일에 주어진 첨두계수 {factor:.1f}를 적용할 때 첨두 유량은? 이 계수는 문제 조건이며 공식 설계기준 값이 아니다.',f'첨두 유량=평균 유량×주어진 계수={base}×{factor:.1f}.',base*factor,[base,factor],'m³/일',j)
 flow=3000+300*j;area=100+10*j
 numeric(2,'표면부하','overflow',f'침전지 유량 {flow} m³/일, 수면적 {area} m²이다. 표면부하율은?',f'표면부하율=Q/A={flow}/{area}.',flow/area,[flow,area],'m³/(m²·일)',j)
 load=200+20*j;vol=500+10*j;mlss=2000+100*j
 numeric(2,'F/M비','fm',f'생물반응조 BOD 부하 {load} kg/일, 용적 {vol} m³, MLSS {mlss} mg/L이다. MLSS 기준 F/M비는?',f'MLSS 질량=V×X/1,000={vol}×{mlss}/1,000 kg. F/M=부하/MLSS 질량.',load/(vol*mlss/1000),[load,vol,mlss],'일⁻¹',j)
 flow=1000+100*j;dose=2+j*.2
 numeric(2,'약품 주입량','dose',f'처리 유량 {flow} m³/일, 주어진 약품 주입 농도 {dose:.1f} mg/L이다. 순수 약품의 일일 주입 질량은? 실제 소독 기준을 뜻하지 않는다.',f'주입 질량=Q×주입 농도/1,000={flow}×{dose:.1f}/1,000.',flow*dose/1000,[flow,dose],'kg/일',j)
 v=500+50*j;x=3000+100*j;waste=50+5*j
 numeric(2,'고형물 체류시간','srt',f'반응조 {v} m³, MLSS {x} mg/L이다. 유출 고형물을 포함한 계외 고형물 배출량은 {waste} kg/일이다. SRT는?',f'보유 고형물=V×X/1,000 kg. SRT=보유량/총 배출량={v}×{x}/1,000/{waste}.',v*x/1000/waste,[v,x,waste],'일',j)
 influent=100+10*j;first=20;second=50
 numeric(2,'연속 제거','series',f'유입 농도 {influent} mg/L에 대해 1단계가 {first}%, 2단계가 잔류분의 {second}%를 제거한다. 부피 변화가 없을 때 최종 농도는?',f'C=C₀(1−r₁)(1−r₂)={influent}×0.8×0.5.',influent*.8*.5,[influent,first,second],'mg/L',j)
 sample=5+j;final=100+10*j;measured=2+j*.2
 numeric(3,'희석 환산','dilution',f'시료 {sample} mL를 {final} mL로 정용했다. 희석액 측정값이 {measured:.1f} mg/L일 때 원시료 농도는? 공시험 보정은 불필요하다.',f'희석배수=최종 부피/시료 부피. 원농도=C측정×배수={measured:.1f}×{final}/{sample}.',measured*final/sample,[sample,final,measured],'mg/L',j)
 slope=.02+j*.002;intercept=.01;absorb=.21+j*.02
 numeric(3,'검량선','calibration',f'검량선 A={slope:.3f}C+{intercept:.2f}에서 C 단위는 mg/L이다. 흡광도 A={absorb:.2f}일 때 C는?',f'C=(A−절편)/기울기=({absorb:.2f}−{intercept:.2f})/{slope:.3f}.',(absorb-intercept)/slope,[slope,intercept,absorb],'mg/L',j)
 original=10+j;added=20;observed=28+j
 numeric(3,'첨가회수율','recovery',f'원시료 {original} mg/L에 {added} mg/L 상당을 첨가했다. 부피 변화가 없고 첨가 후 측정값이 {observed} mg/L라면 회수율은?',f'회수율=(첨가 후−첨가 전)/첨가량×100=({observed}−{original})/{added}×100.',(observed-original)/added*100,[original,added,observed],'%',j)
 d1=8+j*.1;d2=5+j*.1;p=.02+j*.002
 numeric(3,'BOD 계산 연습','bod',f'식종 보정이 필요 없는 희석 시료의 초기 DO {d1:.1f} mg/L, 5일 후 DO {d2:.1f} mg/L, 원시료 부피분율 P={p:.3f}이다. 단순 BOD₅ 계산값은? 채취·보존 적합성은 별도이며 본 문제는 계산만 다룬다.',f'BOD₅=(D₁−D₂)/P=({d1:.1f}−{d2:.1f})/{p:.3f}.',(d1-d2)/p,[d1,d2,p],'mg/L',j)
 before=50+j;after=50.01+j;volume=100+10*j
 numeric(3,'중량농도','gravimetric',f'여과 전 건조 필터 {before:.2f} g, 여과·건조 후 {after:.2f} g, 여과 시료 {volume} mL이다. 공시험 보정 없이 부유물질의 질량농도는?',f'증가 질량을 mg, 부피를 L로 바꾼다. C=(후−전)×1,000,000/시료mL=({after:.2f}−{before:.2f})×1,000,000/{volume}.',(after-before)*1e6/volume,[before,after,volume],'mg/L',j)
concepts=[
('기준 확인','법규 수치를 학습 자료에 적을 때 가장 적절한 검증 방법은?','관할 공식 법령의 시행일·별표·적용 대상을 함께 확인한다','검색 결과 요약만 복사한다','오래된 블로그 숫자를 최신으로 표시한다','서로 다른 시설의 수치를 섞는다','법령 수치는 적용 시점과 대상에 따라 달라질 수 있으므로 원문과 시행일을 대조해야 한다.'),
('농도와 총량','농도 기준과 오염물질 총량의 차이를 설명한 것은?','총량은 농도뿐 아니라 배출 유량에도 좌우된다','총량과 농도의 단위는 항상 같다','유량은 총량에 영향을 주지 않는다','같은 농도이면 총량은 언제나 같다','질량부하=농도×유량이므로 농도만으로 총량을 판단할 수 없다.'),
('배출 기록','측정 기록의 추적 가능성을 높이는 방법은?','채취 시각·지점·방법과 원자료를 연결하여 보존한다','최종 평균값만 남기고 원자료를 지운다','초과값은 설명 없이 삭제한다','시료명을 모두 같게 적는다','시료와 분석 결과를 연결하는 원자료가 있어야 검토와 재확인이 가능하다.'),
('대표성','배출수 시료의 대표성에 대한 올바른 접근은?','공식 적용 방법과 배출 특성을 확인해 채취 계획을 세운다','가장 깨끗해 보이는 순간만 선택한다','채취 지점은 기록할 필요가 없다','분석 기기만 좋으면 채취 방식은 무관하다','채취 위치·시각·방법은 분석값의 대표성을 좌우한다. 구체 방법은 해당 공식 기준을 확인해야 한다.'),
('허가 조건','시설에 적용할 관리 조건을 확인하는 적절한 방법은?','해당 시설의 허가·신고 내용과 적용 법령을 함께 대조한다','다른 시설의 조건을 그대로 쓴다','업종만 비슷하면 조건도 같다','인터넷 댓글을 최종 근거로 삼는다','시설의 조건과 현행 법령의 적용 범위를 각각 확인해야 한다.'),
('기준의 종류','수역 환경의 목표와 배출구 관리 기준을 구별해야 하는 이유는?','관리 대상과 평가 목적이 다를 수 있기 때문이다','둘은 반드시 동일 수치이기 때문이다','하천에는 오염물질이 없기 때문이다','배출구 유량은 측정할 수 없기 때문이다','수역의 상태와 개별 배출행위를 관리하는 기준은 목적과 적용 지점을 구별하여 읽어야 한다.'),
('개정 관리','시행 전 개정 규정과 현행 규정을 혼동하지 않으려면?','공포일과 시행일·경과조치를 구분한다','공포된 즉시 모든 조항이 적용된다고 가정한다','제목만 확인한다','별표는 확인하지 않는다','공포일과 시행일은 다를 수 있으며 경과조치도 적용 판단에 중요하다.'),
('정보 표시','출처가 확인되지 않은 법정 수치를 문제은행에서 처리하는 적절한 방법은?','검증 대기로 두고 현행 기준이라고 단정하지 않는다','임의 수치로 빈칸을 채운다','기출로 표시한다','연도를 만들어 붙인다','확인되지 않은 수치는 검증 완료로 유통하지 않아야 한다.'),
('단위 대조','측정값과 한계값을 비교하기 전에 확인할 것은?','항목·단위·적용 조건의 일치 여부','숫자 크기만 비교하면 된다','측정 단위는 아무거나 써도 된다','서로 다른 항목의 평균을 낸다','같은 항목·단위·조건이어야 수치 비교가 의미를 가진다.'),
('시료 인계','시료 인계 기록의 주된 목적은?','누가 언제 어떤 시료를 취급했는지 추적하기 위함','분석을 생략하기 위함','농도를 낮추기 위함','모든 시료의 보존 기간을 같게 만들기 위함','시료의 취급 이력은 결과의 신뢰성과 추적 가능성을 지원한다.'),
('오염 방지','사고 유출 대응 계획에서 우선 고려할 관리 원칙은?','인명 안전과 추가 유출 방지·확산 억제를 준비한다','희석해서 기록을 없앤다','다른 배출구로 옮기면 문제가 사라진다','시료를 버려 원인을 알 수 없게 한다','안전 확보와 오염 확산 억제가 중요하다. 구체 신고 절차와 기한은 적용 법령을 별도 확인해야 한다.'),
('농도 환산','mg/L와 kg/일을 직접 같은 기준값처럼 비교할 수 없는 이유는?','농도와 단위 시간당 질량이라는 서로 다른 물리량이다','두 단위는 철자만 다르다','물은 질량이 없기 때문이다','둘 다 무조건 백분율이기 때문이다','농도에서 부하량으로 환산하려면 유량이 필요하다.'),
('초과값 검토','측정 초과값이 나왔을 때 자료 관리상 적절한 행동은?','원자료를 보존하고 측정 조건·절차와 적용 기준을 검토한다','수치를 임의 수정한다','시료 이름을 지운다','평균이 낮아질 때까지 임의 자료를 추가한다','원자료를 보존한 검토가 필요하며 임의 삭제나 수정은 추적 가능성을 해친다.'),
('공식 출처','법령 근거로 가장 적절한 자료는?','공식 법령 원문과 해당 별표','출처 없는 그림','AI 응답만','게시 날짜 없는 개인 댓글','AI나 2차 자료는 탐색에 도움을 줄 수 있지만 공식 원문 검증을 대체하지 않는다.'),
('기록 정정','측정 기록을 정정할 때 적절한 방법은?','정정 사유와 이력을 남겨 원기록을 추적할 수 있게 한다','원값을 흔적 없이 덮어쓴다','불리한 기록만 지운다','모든 시각을 임의로 바꾼다','원기록·변경 사유·수정 이력의 추적 가능성을 유지해야 한다.'),
('관할 확인','신고 대상 기관을 학습할 때 적절한 확인 방법은?','적용 법령과 시설 관할을 공식 안내에서 대조한다','가까운 민간 업체로 정한다','다른 자격증의 답을 복사한다','기관 이름을 추정해 만든다','관할과 절차는 적용 대상과 공식 안내로 확인해야 한다.'),
('복수 항목','서로 다른 오염 항목의 수치를 취급하는 올바른 원칙은?','항목마다 정의·측정 방법·기준을 구분한다','BOD와 모든 유해물질을 같은 것으로 본다','단위가 같으면 물질도 같다','분석 항목명은 생략한다','같은 mg/L라도 어떤 물질·측정 방법인지에 따라 의미가 다르다.'),
('시설 관리','처리시설의 정상 운전 여부를 추적하는 데 도움이 되는 기록은?','운전 조건·약품 사용량·유량·측정 결과의 시계열','최저 농도 하나만 적은 메모','아무 시각도 없는 사진 한 장','장비 이름만 적은 목록','운전 상태와 결과를 연결한 시계열은 이상 원인 분석과 관리에 유용하다.'),
('법규 해설','법규 해설의 확인 범위를 정직하게 표시한 것은?','공식 원문 미대조이면 미대조 사실과 적용 한계를 적는다','계산 테스트만 통과하면 최신 법령 준수라고 쓴다','읽지 않은 별표를 검토했다고 적는다','전문가가 보지 않아도 전문가 검수라 쓴다','계산 검증·원문 대조·전문가 검수는 서로 다른 확인 절차이다.'),
('변경 확인','시설 조건이 바뀌었을 때 적절한 관리 접근은?','변경 내용과 적용 절차·기준을 공식 자료로 다시 확인한다','이전 조건이 영구히 유지된다고 가정한다','다른 시설 문서를 이름만 바꿔 사용한다','기록을 모두 삭제한다','변경 내용에 따른 적용 여부를 확인해야 하며 구체 의무는 현행 원문과 관할 안내를 대조해야 한다.'),
]
for j,(topic,stem,right,a,b,c,explain) in enumerate(concepts):
 choices=[right,a,b,c];offset=j%4;choices=choices[offset:]+choices[:offset]
 add(4,topic,stem,explain+' 이 문항은 일반 관리 원칙 연습이며 특정 현행 조항·수치의 확인을 뜻하지 않는다.',choices,choices.index(right)+1)
from expanded_bank import expand
expand(numeric)
assert len(BANK) == 1000
(ROOT/'src/data/questions.json').write_text(json.dumps(BANK,ensure_ascii=False,indent=2)+'\n')
# Import templates are examples, always pending on import.
q={**BANK[0],'id':'LOCAL-W-001','verificationStatus':'pending','reviewNote':'출처·이용 조건·정답 검토 후 승인하세요.'}
(ROOT/'public/templates/questions.json').write_text(json.dumps([q],ensure_ascii=False,indent=2)+'\n')
cols=['id','subject','topic','question','choice1','choice2','choice3','choice4','answer','explanation','difficulty','year','session','type','sourceUrl','verificationStatus','reviewNote','version','rights']
with (ROOT/'public/templates/questions.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=cols,lineterminator="\n");w.writeheader();row={k:q.get(k) for k in cols};row.update({f'choice{i+1}':v for i,v in enumerate(q['choices'])});w.writerow(row)
print('Generated',len(BANK),'questions; numeric 980 (20 families × 10 + 26 families × 30), conceptual 20; shortfall',1000-len(BANK))
