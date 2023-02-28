# EC3216_Automata_Assignment
2022년 봄학기 오토마타 이론 강의 프로그래밍 과제입니다.
## PA1
NFA를 시뮬레이션합니다.<br>
` python simnfa.py nfa.txt in1.txt out.txt `로 실행하며 nfa와 입력파일을 받고 out.txt로 accept/reject를 출력합니다.<br>
입력 파일 첫줄에 입력 문자열을 입력합니다(공백 제외).

NFA 파일 형식은 다음과 같습니다.<br>
```
nfa {상태개수} 1 {끝상태개수} {문자개수} {규칙개수}
{띄어쓰기로 구분된 state 이름}
{init state}
{띄어쓰기로 구분된 final state 이름}
{띄어쓰기로 구분된 문자들}
{이전state} {입력문자} {전이state}
{이전state} {입력문자} {전이state}
...
```
예시로 들어있는 NFA는 (숫자)%, $(숫자), spam 그리고 buy가 포함된 문자열을 accept하는 NFA입니다.<br> 정규 표현식으로 `/[a-z0-9\$%]*(buy|spam|[0-9]+%|\$[0-9]+)[a-z0-9\$%]*/` 이 됩니다.
## PA2
주어진 CFG로 생성할 수 있는 모든 문자열을 생성하고, 주어진 길이 내에서 CFG의 ambiguity를 판정합니다.<br>
`python amb.py 문법파일 최대길이 판정길이 [즉시종료]`
로 실행하며 ambiguity 판정 시 모호함이 발견되면 즉시 종료하는 `즉시종료`값은 기본 true입니다. false를 지정하면 `판정길이` 내의 모든 string을 테스트합니다.

CFG의 예시는 `test_amb.txt` 와 `test_unamb.txt`를 참조해주세요.

예시) `python amb.py test_amb.txt 10 12 false`
```bash
200 strings generated
515 strings tested
Ambiguous Grammar
```
[문자열 출력결과](./PA2/strings.txt), [모호검사 출력 결과](./PA2/tested_ambiguity.txt)





