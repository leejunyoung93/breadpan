Bread pan
========

Bread pan : 기본적인 웹서비스를 간단하게 만드는 프로젝트 틀. 이 프로젝트를 Clone해서 이름을 바꿔서 진행하기를 권장한다. 

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQf-dHcXXifrSmL6RBJG5hdggKjvlcko0Or4IZW2j-myy2kTUbD&s" width="500px" title="Bread pan" alt="BreadPan"/>


기본 사용 도구 
--------
- Front-end
   * React
   * Typescript
   * SAAS
   * 간단한 Dashboard template

- Back-end 
  * Python 3.x
  * Flask

- 자동화 도구
  * make


설계 기본 구조
-----------
* Clean architecture[[en](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)/[kr](https://blog.coderifleman.com/2017/12/18/the-clean-architecture/)]의 기본 개넘에 따라, 최대한 정책에 집중하고 세부사항은 다양하게 될 수 있도록 한다.

<img src="https://blog.cleancoder.com/uncle-bob/images/2012-08-13-the-clean-architecture/CleanArchitecture.jpg" width="500px"  title="Clean architecture" alt="CleanArchitecture"/>

* 프레임워크에 최대한 독립적이 될 수 있게 했다 
* 아래의 4개 계층으로 나눠지게 된다. 
    - EBR(Enterprise Business Rules): 실제 Business logic에서 사용하는 데이터들을 표현 
    - ABR(Application Business Rules): 실제 Business logic의 행위를 이곳에 표현 
    - IA(Interface Adapter): 들어오는 입력을 ABR에 전달하고 ABR의 결과를 외부 Framework에 맞춰서 전달
    - Framework : 실제 사용자 입력을 받고 출력을 하는 inteface
* Back-end / Front-end의 경계는? 
   - Front-end: Framework / Interface adapter의 한 축으로 제일 변화가 많은 부분이 된다.
        - 특별히 React의 특징상, Front-end는 화면에 보여주는 View에 대해서만 다룬다.
   - Back-end: 나머지 것들을 최대한 표현. 
        - 특별히 데이터 저장소의 경우 추상화를 통해서 다양한 Data저장방식으로 이용이 가능해야 한다.

실행하고 테스트 하기 
----------


```bash 
$ make run  # 전체 실행 
```

```bash 
$ make run-fe  # Front-end 실행 
```

```bash
$ make build-fe # Front-end build
```


```shell
python -m unittest discover be_tests # Back-end test
```
