HungryOsori-PushServer
==========================================
작동 순서
------------------------------------------
	크롤링 
	-> 변경사항이 있는지 확인
	-> T: 변경된 파일명을 API에 넘기기  F: 종료
	-> API에서 구독자 명단(token) 받기
	-> token과 변경된 데이터를 Firebase에 넘기기
  

1.크롤링 	
-------------------------------------------
	크론텝으로 3시간 주기로 크롤링을 한다.
	
- 크롤링 파일 목록

Data|Description
---|---
0 |	스팀 세일
1 |	네이버 실시간 랭킹
2 |	남도학숙 식단


2. 변경사항이 있는지 확인
-------------------------------------------
	크롤링 전에 data_base에 저장된 제목들(10개)과 크롤링 후에 저장된 제목들(10개)을 비교해 변경된 사항이 있는지 확인
	변경사항이 있는 경우, 3을 실행
	변경사항이 없는 경우, 종료

3. 변경된 파일명을 API에 넘긴다.
-------------------------------------------

4. API에서 구독자 명단(token) 받기
-------------------------------------------
	API서버 주소랑 크롤러 번호를 넘기고 그에 맞는 구독자 명단(token)을 받는다.

5.token과 변경된 데이터를 Firebase에게 넘긴다. 
-------------------------------------------
	android와 IOS는 데이터 형식이 다르기 때문에 구분하여 token과 데이터를 넘긴다.
