import {test, expect} from '@playwright/test';
for(const spec of [
 {name:'작은 높이',width:390,height:480,zoom:false},
 {name:'가로 모드',width:740,height:360,zoom:false},
 {name:'일반 세로',width:390,height:844,zoom:false},
 {name:'확대 글자',width:390,height:480,zoom:true},
]) {
 test(`${spec.name}: 실제 입력으로 하단 도구·상단 대시보드 접근`,async({page,isMobile})=>{
  await page.setViewportSize({width:spec.width,height:spec.height});await page.goto('');
  if(spec.zoom)await page.addStyleTag({content:'html {font-size:125%} .sidebar {font-size:125%} .sidebar nav button {font-size:1em}'});
  await page.getByRole('button',{name:'메뉴 열기'}).click();
  const sidebar=page.locator('.sidebar'); await expect(sidebar).toHaveClass(/open/);
  await page.waitForTimeout(450); // wait for CSS slide animation before input coordinates
  const cdp=isMobile?await page.context().newCDPSession(page):null;
  async function move(down:boolean) {
   if(cdp){
    const start=down?spec.height-70:90,end=down?80:spec.height-70;
    await cdp.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x:130,y:start}]});
    for(let i=1;i<=12;i++) {
     await cdp.send('Input.dispatchTouchEvent',{type:'touchMove',touchPoints:[{x:130,y:start+(end-start)*i/12}]});
     await page.waitForTimeout(16);
    }
    await cdp.send('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});
   }else{await page.mouse.move(130,Math.min(220,spec.height-30));await page.mouse.wheel(0,down?500:-500);}
   await page.waitForTimeout(200);
  }
  const overflow=await sidebar.evaluate(e=>e.scrollHeight>e.clientHeight);
  for(let i=0;i<5;i++)await move(true);
  if(overflow)expect(await sidebar.evaluate(e=>e.scrollTop)).toBeGreaterThan(0);
  const backup=page.getByRole('button',{name:'학습 기록 백업',exact:true});
  const reset=page.getByRole('button',{name:'데이터 초기화',exact:true});
  for(const locator of [backup,reset]) {
   const box=await locator.boundingBox();expect(box).not.toBeNull();expect(box!.y).toBeGreaterThanOrEqual(0);expect(box!.y+box!.height).toBeLessThanOrEqual(spec.height);
  }
  const download=page.waitForEvent('download');await backup.click();expect((await download).suggestedFilename()).toContain('water-environment');
  await reset.click();await expect(page.getByRole('dialog')).toBeVisible();await page.getByRole('button',{name:'돌아가기',exact:true}).click();
  for(let i=0;i<5;i++)await move(false);
  await expect.poll(()=>sidebar.evaluate(e=>e.scrollTop)).toBe(0);
  const home=page.getByRole('navigation').getByRole('button',{name:'학습 대시보드',exact:true});
  const box=await home.boundingBox();expect(box!.y).toBeGreaterThanOrEqual(0);expect(box!.y+box!.height).toBeLessThanOrEqual(spec.height);
  await home.click();await expect(sidebar).not.toHaveClass(/open/);
  await expect(page.getByRole('heading',{name:'수질환경기사 필기 CBT',exact:true})).toBeVisible();
  expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);
 });
}
test('모든 주요 화면의 상단 상시 배너 부재·저장 실패 경고 유지',async({page})=>{
 await page.goto('');
 for(const label of ['실전 모의시험','랜덤 문제풀이','오답노트','북마크','학습 통계','문제은행 관리','학습 대시보드']){
  if(await page.getByRole('button',{name:'메뉴 열기'}).isVisible()) await page.getByRole('button',{name:'메뉴 열기'}).click();
  await page.getByRole('navigation').getByRole('button',{name:label,exact:true}).click();
  await expect(page.locator('.criteria-note')).toHaveCount(0);
  if(label!=='문제은행 관리') await expect(page.locator('main')).not.toContainText(/공식 출제기준 대조 대기|잠정 규칙|기출 미제공/);
 }
 await page.evaluate(()=>{Storage.prototype.setItem=()=>{throw new DOMException('Quota exceeded','QuotaExceededError')}});
 await page.getByRole('button',{name:'문제풀이 시작하기'}).click();
 await expect(page.getByRole('alert')).toContainText('기록을 저장하지 못했습니다');
});
