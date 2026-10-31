"""780 new authored numeric conditions; 26 families × 30. No legal limits."""
import math

def expand(numeric):
 for j in range(30):
  # 수질오염개론: 산염기·경도·반응·혼합·산소
  h=(j+1)*1e-6
  numeric(0,'수소이온과 pH','ph',f'이상적 묽은 수용액의 수소이온 농도가 {h:.9f} mol/L이다. 활동도 보정을 무시한 pH는?',f'pH=−log₁₀[H⁺]=−log₁₀({h:.9f}).',-math.log10(h),[h],'',j)
  ph=4+j*.1
  numeric(0,'pH와 pOH','poh',f'25 ℃에서 pH가 {ph:.1f}인 이상적 수용액이다. pKw=14로 주어질 때 pOH는?',f'pH+pOH=pKw이므로 pOH=14−{ph:.1f}.',14-ph,[ph],'',j)
  c=100+3*j;k=.05+j*.002;t=4+j*.1
  numeric(0,'1차 반응','first-order',f'초기 농도 {c} mg/L의 물질이 속도상수 {k:.3f} 일⁻¹의 1차 반응으로 감소한다. {t:.1f}일 후 농도는?',f'dC/dt=−kC를 적분하면 C=C₀e^(−kt)={c}×exp(−{k:.3f}×{t:.1f}).',c*math.exp(-k*t),[c,k,t],'mg/L',j)
  v=10+j;ci=80+j;target=20
  numeric(0,'희석수 필요량','diluent',f'농도 {ci} mg/L인 물 {v} m³에 물질을 포함하지 않은 물을 넣어 {target} mg/L로 만들려 한다. 반응과 부피 수축이 없을 때 추가할 물의 부피는?',f'질량보존 CᵢV=C목표(V+V추가). V추가=V(Cᵢ/C목표−1)={v}×({ci}/{target}−1).',v*(ci/target-1),[v,ci,target],'m³',j)
  alk=30+3*j
  numeric(0,'알칼리도 당량','alkalinity',f'알칼리도가 CaCO₃ 환산 {alk} mg/L이다. CaCO₃의 당량 질량을 50 mg/meq로 주었을 때 알칼리도는?',f'meq/L=(mg/L as CaCO₃)/(50 mg/meq)={alk}/50.',alk/50,[alk],'meq/L',j)
  ca=10+j;mg=5+j*.3
  numeric(0,'칼슘·마그네슘 경도','hardness',f'Ca²⁺ {ca} mg/L, Mg²⁺ {mg:.1f} mg/L인 물이다. Ca 경도 환산계수 2.5, Mg 경도 환산계수 4.1을 사용할 때 총경도(CaCO₃ 환산)는? 다른 경도 성분은 없다.',f'주어진 환산계수에 따라 총경도=2.5[Ca]+4.1[Mg]=2.5×{ca}+4.1×{mg:.1f}.',2.5*ca+4.1*mg,[ca,mg],'mg/L',j)
  sat=9+j*.02;do=3+j*.05
  numeric(0,'산소 부족량','oxygen-deficit',f'해당 수온·조건의 포화 DO가 {sat:.2f} mg/L이고 실제 DO는 {do:.2f} mg/L이다. 포화 상태에 대한 산소 부족량은?',f'부족량=D포화−DO실제={sat:.2f}−{do:.2f}.',sat-do,[sat,do],'mg/L',j)
  # 상하수도계획: 수리·양수·수요
  q=.1+j*.005;vel=1+j*.02
  numeric(1,'원형관 직경','diameter',f'만관 원형관에 유량 {q:.3f} m³/s를 평균 유속 {vel:.2f} m/s로 흘린다. 필요한 내경은? π는 원주율을 사용한다.',f'Q=vπD²/4에서 D=√(4Q/(πv))=√(4×{q:.3f}/(π×{vel:.2f})).',math.sqrt(4*q/(math.pi*vel)),[q,vel],'m',j)
  n=.013;r=.2+j*.005;slope=.001+j*.00002
  numeric(1,'Manning 평균 유속','manning',f'Manning 조도계수 n={n}, 동수반경 R={r:.3f} m, 에너지 경사 S={slope:.5f}이다. SI 단위 Manning 식으로 구한 평균 유속은?',f'v=(1/n)R^(2/3)S^(1/2)=(1/{n})×{r:.3f}^(2/3)×√{slope:.5f}.',r**(2/3)*math.sqrt(slope)/n,[n,r,slope],'m/s',j)
  q=.02+j*.001;head=10+j;eff=.7
  numeric(1,'펌프 축동력','pump',f'물의 밀도 1,000 kg/m³, g=9.81 m/s², 유량 {q:.3f} m³/s, 총양정 {head} m, 펌프 효율 {eff}이다. 필요한 펌프 축동력은? 전동기 손실은 별도이다.',f'축동력=ρgQH/η. W에서 kW로 변환하면 9.81QH/η=9.81×{q:.3f}×{head}/{eff}.',9.81*q*head/eff,[q,head,eff],'kW',j)
  pop=20000+100*j;growth=.01+j*.0002;years=5
  numeric(1,'등비 인구 추계','population',f'현재 인구 {pop}명, 매년 일정 증가율 {growth*100:.2f}%, 기간 {years}년이다. 등비 증가를 가정한 추계 인구는? 계산 연습이므로 인원도 소수 셋째 자리로 표시한다.',f'Pₙ=P₀(1+r)ⁿ={pop}×(1+{growth:.4f})^{years}.',pop*(1+growth)**years,[pop,growth,years],'명',j)
  water=3000+50*j;fraction=.7+j*.003
  numeric(1,'오수 전환율','sewage',f'급수량 {water} m³/일 중 {fraction*100:.1f}%가 오수로 유입된다. 침입수·유입수를 무시할 때 오수량은? 비율은 주어진 연습 조건이다.',f'오수량=급수량×전환율={water}×{fraction:.3f}.',water*fraction,[water,fraction],'m³/일',j)
  vol=5000+100*j;daily=1000+10*j
  numeric(1,'저수 지속일수','supply-days',f'이용 가능한 저수량 {vol} m³, 일정한 수요 {daily} m³/일이다. 추가 유입과 손실이 없을 때 공급 가능한 기간은?',f'지속일수=이용 가능 용량/일 수요={vol}/{daily}.',vol/daily,[vol,daily],'일',j)
  supplied=10000+100*j;metered=8000+50*j
  numeric(1,'수량 손실 비율','water-loss',f'일일 공급량 {supplied} m³, 같은 경계·기간의 계량 사용량 {metered} m³이다. 다른 용도가 없다고 가정할 때 미계량 차이의 공급량 대비 비율은? 실제 누수율과 반드시 같다는 뜻은 아니다.',f'차이 비율=(공급−계량)/공급×100=({supplied}−{metered})/{supplied}×100.',(supplied-metered)/supplied*100,[supplied,metered],'%',j)
  # 방지기술: 부하·여과·슬러지·반송·반응 설계
  q=1000+30*j;ci=120+j;co=20+j*.2
  numeric(2,'제거 질량부하','removed-load',f'처리 유량 {q} m³/일, 유입 BOD {ci} mg/L, 유출 BOD {co:.1f} mg/L이다. 유량 변화가 없을 때 제거한 BOD 질량은?',f'제거 질량=Q(Cᵢ−Cₑ)/1,000={q}×({ci}−{co:.1f})/1,000.',q*(ci-co)/1000,[q,ci,co],'kg/일',j)
  q=1000+20*j;rate=4+j*.1
  numeric(2,'여과 면적','filter-area',f'여과 처리량 {q} m³/일, 주어진 여과속도 {rate:.1f} m/시간이다. 24시간 연속 운전하고 예비 면적을 제외할 때 필요한 유효 여과 면적은?',f'시간당 유량=Q/24. 면적=Q/(24v)={q}/(24×{rate:.1f}).',q/(24*rate),[q,rate],'m²',j)
  wet=1000+25*j;solids=.02+j*.001
  numeric(2,'슬러지 건고형물','dry-solids',f'습윤 슬러지 {wet} kg/일의 고형물 질량분율은 {solids:.3f}이다. 포함된 건고형물의 질량은?',f'건고형물=습윤 질량×고형물 질량분율={wet}×{solids:.3f}.',wet*solids,[wet,solids],'kg/일',j)
  cod=200+10*j;factor=.6+j*.005
  numeric(2,'산소량 환산 연습','oxygen-demand',f'제거 COD 부하가 {cod} kg/일이다. 이 문제에서는 산소 필요량을 제거 COD 1 kg당 {factor:.3f} kg O₂로 가정한다. 산소 필요량은? 실제 시설 산소 설계를 대신하지 않는다.',f'주어진 가정에 따라 O₂ 요구량=제거 COD×계수={cod}×{factor:.3f}.',cod*factor,[cod,factor],'kg O₂/일',j)
  x=2000+20*j;xr=8000+30*j
  numeric(2,'반송 슬러지 비율','recycle',f'반응조 MLSS X={x} mg/L, 반송 슬러지 농도 Xr={xr} mg/L이다. 유입 고형물·유출 고형물·잉여슬러지를 무시한 정상상태 침전지 수지에서 Qr/Q는?',f'(Q+Qr)X=QrXr에서 Qr/Q=X/(Xr−X)={x}/({xr}−{x}).',x/(xr-x),[x,xr],'배',j)
  ci=100+j;co=10+j*.1;k=.2+j*.005
  numeric(2,'1차 반응 소요시간','reaction-time',f'회분식 1차 반응에서 농도 {ci} mg/L를 {co:.1f} mg/L로 줄이려 한다. 반응속도상수 {k:.3f} 시간⁻¹일 때 필요한 시간은?',f'C/C₀=e^(−kt)이므로 t=ln(C₀/C)/k=ln({ci}/{co:.1f})/{k:.3f}.',math.log(ci/co)/k,[ci,co,k],'시간',j)
  # 공정시험: 공식 절차/법정 값이 아닌 주어진 실험 조건의 계산
  titrant=2+j*.1;normal=.02;sample=100+j
  numeric(3,'당량 적정 환산','titration',f'공시험 보정 후 산 소비량 {titrant:.1f} mL, 산의 노르말농도 {normal} eq/L, 시료 {sample} mL이다. CaCO₃ 당량 질량 50 g/eq로 주었을 때 알칼리도 환산값은?',f'CaCO₃ mg/L=적정mL×N×50,000/시료mL={titrant:.1f}×{normal}×50,000/{sample}.',titrant*normal*50000/sample,[titrant,normal,sample],'mg/L',j)
  a=20+j;b=22+j*1.1
  numeric(3,'상대 백분율 차이','rpd',f'중복 분석값이 {a} mg/L와 {b:.1f} mg/L이다. 평균값 기준 상대 백분율 차이 RPD는? RPD=절대차/평균×100으로 정의한다.',f'RPD=|x₁−x₂|/((x₁+x₂)/2)×100=|{a}−{b:.1f}|/(({a}+{b:.1f})/2)×100.',abs(a-b)/((a+b)/2)*100,[a,b],'%',j)
  a=10+j;b=12+j*.8;c=14+j*.6
  numeric(3,'산술평균','sample-mean',f'같은 시료의 세 측정값이 {a} mg/L, {b:.1f} mg/L, {c:.1f} mg/L이다. 동일 가중치 산술평균은?',f'평균=(x₁+x₂+x₃)/3=({a}+{b:.1f}+{c:.1f})/3.',(a+b+c)/3,[a,b,c],'mg/L',j)
  a=10+j;b=12+j;c=16+j
  numeric(3,'표본 표준편차','sample-sd',f'세 측정값이 {a}, {b}, {c} mg/L이다. 분모가 n−1인 표본 표준편차는?',f'평균 x̄=({a}+{b}+{c})/3. s=√(Σ(xᵢ−x̄)²/(3−1)).',math.sqrt(sum((v-(a+b+c)/3)**2 for v in [a,b,c])/2),[a,b,c],'mg/L',j)
  measured=.3+j*.01;blank=.02+j*.0005;slope=.03
  numeric(3,'공시험 신호 보정','blank-calibration',f'시료 흡광도 {measured:.4f}, 공시험 흡광도 {blank:.4f}이다. 공시험 보정 후 신호의 검량선이 A보정={slope}C이며 C 단위는 mg/L이다. 농도는?',f'C=(A시료−A공시험)/기울기=({measured:.4f}−{blank:.4f})/{slope}.',(measured-blank)/slope,[measured,blank,slope],'mg/L',j)
  measured=4+j*.08;sat=9+j*.01
  numeric(3,'DO 포화율','do-percent',f'측정 DO가 {measured:.2f} mg/L이고 해당 수온·압력에서 포화 DO가 {sat:.2f} mg/L로 주어졌다. DO 포화율은?',f'포화율=실측 DO/포화 DO×100={measured:.2f}/{sat:.2f}×100.',measured/sat*100,[measured,sat],'%',j)
