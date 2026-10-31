export const PROFILE = {
  name: "수질환경기사", slug: "water-environmental-engineer",
  subjects: ["수질오염개론", "상하수도계획", "수질오염방지기술", "수질오염공정시험기준", "수질환경관계법규"],
  questionCount: 100, perSubject: 20, durationMinutes: 150,
  choices: 4, passScore: 60, subjectCutoff: 40,
  storageKey: "water-environmental-engineer-cbt:v1",
  rulesStatus: "공식 대조 미완료: 학습용 잠정 설정",
  officialSource: "https://www.q-net.or.kr/crf005.do?id=crf00503&jmCd=1662",
} as const;
