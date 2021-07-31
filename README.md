# WalkBook 🏃‍♂️🏃‍♀️
> SNU LikeLion 9th Hackerthon - 워크북(walkBook)
✅ "함께 길을 읽다, 워크북"
<img src="https://user-images.githubusercontent.com/76577426/126854973-76a95cd5-cd65-4e14-89cf-01dd4825c455.png"  width="700" height="370">

✅ 기획의도
---
- 코로나로 인해 여가시간은 늘었으나 활동 범위가 제한되면서 **동네 산책**이 새로운 여가활동 중 하나로 주목받았습니다.

- 그러나 집 근처 산책로에 대한 정보를 공유할 수 있는 곳이 마땅치 않아 평소에 다녔던 곳만 반복해서 걷게 되고, 다른 사람들과 경험을 공유하기 힘들다 보니 산책에 대한 흥미를 지속적으로 유지하기 어렵다는 한계가 존재했습니다.

- **워크북**은 이러한 한계를 극복하고 위치별 산책로에 대한 정보와 함께 각자의 긍정적인 경험을 공유할 수 있는 비대면 공간을 만들고자 기획된 웹서비스입니다.
    
✅ 주요 서비스 플로우
---
1. 집 주변 새로운 산책로에 대한 정보를 얻거나 본인이 발견한 산책로를 등록하고 싶은 사용자가 **회원가입**을 합니다. 회원가입은 구글로그인으로도 가능합니다.  

2. 다른 사람들이 등록한 산책로를 지도 상에서 보고 싶은 사용자는 ‘**지도에서 찾기**’를, 포스트 형식으로 정보를 보고 싶은 사용자는 ‘**게시판에서 찾기**’ 버튼을 누릅니다. 두 페이지 모두에서 원하는 주제의 제목이나 내용을 담은 산책로가 있는지 검색할 수 있습니다.  

3. ‘지도에서 찾기’를 누른 사용자는 회원가입 시 입력한 주소를 중심으로 한 지도 상에서 다른 사람들이 등록한 산책로들을 볼 수 있습니다. 그중 관심 가는 산책로 위에 커서를 올리면 해당 산책로의 이름, 소요시간, 소개, 좋아요 개수를 담은 인포윈도우를 볼 수 있습니다. 더 자세한 정보를 원할 경우 클릭을 해서 해당 산책로의 총거리, 출발위치, 도착위치, TMI를 담은 게시글로 이동합니다. 산책로가 마음에 들면 좋아요를 누르거나 댓글을 남길 수 있습니다.  

4. ‘게시판에서 찾기’를 누른 사용자는 인포윈도우와 동일한 정보를 보여주는 게시글들이 정렬된 게시판으로 이동합니다. 좋아요순이나 최신순으로 게시글 정렬 순서를 바꿀 수 있습니다. 인기가 좋거나 마음에 드는 게시글 제목을 클릭하면 해당 글로 이동해 좋아요를 누르거나 댓글을 남길 수 있습니다. 산책로 작성자의 닉네임을 클릭하면 그 사람의 워크북을 방문해볼 수도 있습니다.  

5. ‘**산책로 등록**’을 통해 ‘나의 워크북’을 만들 수 있습니다. 화면상의 설명에 맞춰 마커와 핀을 입력하고, 산책로의 정보를 입력하고 등록하세요. 지도와 게시판에서 마음에 드는 산책로를 발견하면 좋아요를 눌러보세요! 내가 등록한 산책로와 좋아하는 산책로는 ‘**나의 워크북**’에서 다시 모아볼 수 있습니다.
  
✅ 기술스택
---
Frontend : Vanila Js, Scss    
Backend : Django    
  
  
✅ Model
---
![image](https://user-images.githubusercontent.com/52378625/126783361-5feb2977-68dc-4e6b-a6d2-cb99a73ec07e.png)


✅ Deploy
---
https://walkbook.herokuapp.com

💚 개발 후기
---
- 예지: 자랑스러운 팀장님! Html, Css를 마스터하고 뭐든 뚝딱 만들어주는 뚝딱좌  
```
정말 행복했던 첫 해커톤! 선물같은 팀원들에게 감사할 따름입니다.. 
정말 든든하게 기본 기능과 디테일을 받쳐준 만능좌 나영언니, 맡은 일을 모두 완벽하게 해와 존경스러웠던 구글좌 세원, 
바쁜 와중에도 완벽하게 할 일을 하고 마지막 목업까지 꾸며준 헤르미온느좌 별이까지! 
제가 부족한 점이 있어도 다 감싸주고 서로 보완해주셔서 고맙다는 말을 전하고 싶어요. 
팀플이 이렇게 즐거워도 되나요~ 싶었습니다! 함께 할 수 있어서 영광이었어요 👩‍👩‍👧‍👧
```

- 별: 몸이 2개라고 해도 믿겠어, 계절 7학점에 해커톤까지 ? 근데 잘해,, 헤르미온느좌  
```
정말 우리 팀원들 다 너무 대단하고 진짜 멋진데 모두가 알아줬으면 좋겠습니다...
어려운 맵 부분도 전혀 어렵지 않게 해결해주고 노션까지 파서 체계적으로 일할 수 있게 해준 불도저 나영언니, 
뭘 물어봐도 바로바로 대답하고 수정해주는 것도 모자라서 틈틈이 엄청난 유머를 던져서 웃게 해준 세원언니, 
그리고 무엇보다 진짜 좋은 주제 생각해내서 이 팀 모아주고 직접 그림 그려서 디자인하는 것도 모자라 엄청난 css들을 뚝딱뚝딱 해낸 예지언니!! 
제가 좀 더 시간을 많이 투자했으면 좋았을 텐데 그러지 못해서 너무 아쉬웠고 죄송합니다..
진짜 세상 사람들 우리 팀원 언니들 잘난 거 알아주고 가세요!!
```

- 나영: 백엔드이지만 js도 마스터해버린,, 모든 일단 하고보는 불도저좌  
```
엄청난 팀원들과 함께한 워크북.. 얼레벌레 개발해서 오류 너무 많이 발견하게 해서 죄송합니다.. 
그래도 정말 challenging한 해커톤이어서 너무 재밌었습니다!  
어떤 문제든 해결책을 찾아내서 너무너무 든든했던 구글좌 세원, 웹페이지를 순식간에 있어보이게 만들어주었던(=있어빌리티) 뚝딱좌 예지,
계절학기 때문에 고생했지만 엄청난 퀄리티의 목업을 만들어준 헤르미온느좌 별이.. 팀워크 너무 좋았던 우리 팀! 정말 행복했습니다 🤍
```
- 세원: 오류? 어림도없지.. 구글링으로 문제를 척척 해결하는 구글좌  
```
아이디어톤부터 배포까지 정말 시간이 훅 지나갔던 것 같아요.  
3주 간 우리 팀원들 너무 고생했고 결과물이 예상보다 잘 나온 것 같아서 뿌듯합니다!! 
출퇴근하면서도 누구보다 열심히 임해줬던 불도저 나영언니, 팀장으로서 잘 이끌어주고 Css의 왕이 되어버린 예지, 
계절 7학점 들으면서도 거뜬히 1인분 이상 해준 별이 고맙습니다! 멋진 팀원들과 함께 할 수 있어서 행복했어요❤  
```


