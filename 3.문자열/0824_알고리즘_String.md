# 0824 String

## 문자열 개요

* 문자열
* 패턴 매칭
  * Brute-force
  * 카프-라빈
  * KMP
  * 무어
* 문자열 암호화
* 문자열 압축
* 실습 1,2



![image-20200826094313456](../etc.보강/요약)



## 문자열

### 문자의 표현

---

* 컴퓨터에서의 문자 표현
  * 글자 A를 메모리에 저장하는 방법에 대해서 생각
  * 메모리는 숫자만을 저장할 수 있기 때문에 A 글자 모양을 비트맵으로 저장하는 방법을 사용하지 않는 한 각 문자에 대해서 대응되는 숫자를 정해놓고 이것을 메모리에 저장하는 방법이 사용
    * 비트맵 저장 방식의 메모리 낭비는 매우 심함
  * 영어 대소문자 합쳐 52이므로 6비트(62가지)면 모두 표현할 수 있음
    * 코드체계라고 부름
    * 000000: 'a', 000001:'b'
  * 코드 체계의 종류
    * 6 bit BCD // 대소 구분 x
    * 7 bit ASCII
    * 8 bit EBCDIC



* ASCII
  * 인터넷, 네트워크의 발달로 지역 간 정보 체계의 통일성, 표준 문제 발생
  * 7bit 인코딩으로 128문자를 표현하며, 33개의 출력 불가능한 제어 문자들과 공백 미롯 95개의 출력 가능한 문자로 이루어짐
    * \0과 같은 null 문자가 33개 존재
  * parity bit와 함께 사용
    * error를 체크하는 bit
    * 1의 개수가 짝수인지, 홀수인지 표시하는 bit자리
  * Byte
    * 알파벳 한 글자를 나타내는 단위
    * = 8bit



* 확장 아스키
  * 문자 표준 이외 악센트 문자, 도형 문자, 특수 문자, 특수 기호 등 부가적 문자를 128개 추가
    * 확장 아스키는 8bit를 모두 사용
    * 컴퓨터 생산자 - 소프트웨어 개발자 합의가 이루어지지 않아 확장 부호는 프로그램, 컴퓨터 사이 교환이 이루어지지 않음
    * 확장 아스키는 인터프리터가 없으면 해독이 안됨



#### 유니코드

---

* 유니코드
  * 현재 전세계 표준
    * 국가별 코드 체계(한국-조합형 / 완성형) 통신 문제
  * 2byte 크기의 완성형 코드체계



* 유니 코드도 다시 Charcter set으로 분류됨

  * UCS - 2
  * UCS - 4
  * 유니코드를 저장하는 변수의 크기를 정의
  * 단, 바이트 순서에 대한 표준화 x
    * Big-endian & little-endian 문제
    * 파일의 Set (UCS-2, UCS-4)을 구분하여 구현해야 하는 문제가 발생함
    * 적당한 **외부 인코딩**이 필요함

  

* Big-endian, little -endian

  * 0000 0000   00110000 = A
  * 0011 0000   0000 0000 =



* 유니코드 인코딩(UTF: Unicode Transformation Format)
  * UTF-8 (in web, python)
    * Min: 8bit, Max: 32bit
    * 1 Byte * 4
    * Python!
  * UTF-16 (in windows, java)
    * Min: 16bit, Max: 32bit
    * 2 Byte * 2
  * UTF-32 (in unix)
    * Min: 32bit, Max: 32bit
    * 4 Byte * 1



* 문자열의 분류
  * flexed length
  * variable length
    * length controlled  (Java언어)
    * delimited (C언어, 구분자)



* java에서 String 클래스에 대한 메모리 배치 예시
  * java.lang.String 클래스에서 기본적 객체 메타 데이터 외에도 네가지 필드가 포함
    * hash(hash 값)
    * count(문자열 길이)
    * offset(문자열 데이터 시작점)
    * value(문자열 배열에 대한 참조)
  * java.lang.String class
    * Class pointer | Flags | Locks | hash | count | offset | value
  * char[]
    * Class pointer | Flags | Locks | size | char ---



* Java(객체지향 언어) 문자열 처리
  * 문자열 데이터를 저장, 처리하는 클래스 제공
    * String class
    * String str="abc";
    * String str = new String("abc")
  * 문자열 처리에 필요한 연산을 연산자, 메소드로 제공
    * +, length(), replace(), split(), substring()...



* C 언어에서 문자열 처리
  * 문자들의 배열 형태로 구현된 '응용 자료형'
  * 문자 배열에 항상 마지막 끝에 \0 (널문자)를 넣어줌
    * char ary[] = {'a','b','c','\0'};
    * char ary[] = "abc";
  * 문자열 처리에 필요한 연산을 함수 형태로 제공
    * strlen(), strcpy(), strcmp()



* C와 Java의 String 처리 기본 차이점
  * c는 아스키 코드
    * char * name = "홍길동";
    * int count = strlen(name);
    * printf("%d", count);
    * 6
  * java는 유니코드(UTF-16)
    * String name = "홍길동";
    * System.out.println(name.length());
    * 3
  * 파이썬 유니코드(UTF-8)
    * name = '홍길동'
    * print(len(name))
    * 3



#### Python 에서의 문자열 처리

---

* Char 타입 없음
  * String
  * 무조건 문자열 처리로 텍스트 데이터 취급 방법이 통일
* 문자열 기호
  * '', "", ''', """
  * 연결(Concatenation)
    * +
    * 문자열 + 문자열로, 이어붙이기
  * 반복(Repeat)
    * *
    * 문자열 * 수 : 수만큼 반복
* 자료형
  * 시퀀스 자료형으로 분류
  * 인덱싱, 슬라이싱 연산 가능
* 문자열 클래스의 메소드
  * replace, split(), isalpha(), find()
* **문자열의 요소 변경**
  * 불가능(immutable)
  * 튜플과 같음



### 문자열 뒤집기

---

> 자기 문자열에서 뒤집는 방법이 있고 
>
> 새로운 빈 문자열을 만들어 소스의 뒤에서부터 읽어서 타겟에 쓰는 방법이 있겠다

* 자기 문자열을 이용할 경우
  * swap을 위한 임시 변수가 필요
  * 반복 수행을 문자열 길이 반 만큼 수행
    * 문자열 길이 9
    * algorithm
    * 9/2 = 4.5
    * 4회 반복
* 연습문제 1
  * c는 알고리즘에 맞추기
  * java는 StringBuffer 클래스의 reverse()메소드
  * python
    * Rerverse 함수
    * slice notation 
      * [::-1]
  * 단, python의 경우 문자열을 list, 배열로 변환 시켜줘야 immutable 속성을 mutable로 만들 수 있음
  * 알고리즘 순서
    * str -> list
      * len(list)
    * swap
      * for 문(길이의 반만큼)
      * arr[0], arr[8] = arr[8] arr[0]
      * ...
    * list -> str
      * "".join(arr)

```python
# 문자열 뒤집기

def str_rev(str):
    # str -> list
    arr = list(str)
    # swap
    for i in range(len(arr)//2):
        arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
    # join
    str = "".join(arr)
    return str

#--------------

ss = "algorithm"
print(ss)
sr = str_rev(ss)
print(sr)

## 슬라이싱싱 연산
print(ss[::-1])


##------------
str2 = "algorithm"
arr2 = list(str2)
arr2.reverse()
str2="".join(arr2)
print(str2)
```



#### 문자열 비교

---

* c strcmp()함수 제공
* Java equals() 메소드
  * 문자열 비교 == 연산은 메모리 참조가 같은지를 묻는것
* 파이썬 == 연산자와 is 연산자
  * ==연산자는 내부 특수 메서드 \__eq__()를 호출
  * 연산자 overloading (c++과 C#도 지원함)
* C 예시
  * *는 포인터

```c
int my_strcmp(const char *str1, const char *str2)
{
    int i =0;
    while(str1[i] != '\0')
    {
        if(str1[i] != str2[i]) break;
        i++;
    }
    return (str1[i] - str2[i]);
}
```

* 파이썬

```python
def strcmp(s1, s2):    # ==와 같은 의미
    if len(s1) != len(s2):
        return False
    else:
        i = 0   # 초기식
        while i < len(s1)  and i < len(s2):#조건식
            if s1[i] != s2[i]:
                return False
            i += 1 # 증감식
        return True

a = "abc"
b = "abc"

print(strcmp(a,b)) # True, False
```



#### 문자열 숫자 정수 변환

---

* c 언어는 atoi()함수 제공

  * 역 함수 itoa()

* java는 숫자 클래스의 parse 메소드

  * Interger.parseInt(String)
  * 역함수 toString() 메소드

* 파이썬 변환 함수 제공

  * int("123")
  * float("3.14")
  * str(123)
    * 식 그대로 표현
  * repr(123)
    * ""을 포함해서 나옴
    * 디버깅 용도

  

* 파이썬 예시

```python
str1 = "123"
str2 = "12.3"

print(int(str1),type(int(str1))) # 123
print(float(str2),type(float(str2))) # 12.3

str3 = "1+2"
print(str3)                      #1+2
print(repr(str3))                #'1+2'
print(eval(str3))                #3
print(eval(repr(str3)))          #1+2
print(eval(eval(repr(str3))))    #3

num1 = 123
num2 = 12.3

print(str(num1),type(str(num1)))   #123
print(repr(num1),type(repr(num1))) #123
print(str(num2),type(str(num2)))   #123
print(repr(num2),type(repr(num2))) #123
```



* C atoi()

```c
int atoi(const char *string)
{
    int value=0, digit, c;
     
    while ((c=*string++) != '\0'){
        if (c >= '0' && c <= '9')
            digit = c - '0';
        else
            break;
        
        value = (value*10) + digit;
    }
    return value;
}

//*string++은 문자열의 주소값을 [1][2][3] 1>2>3 씩 하나씩 옮겨가면서 전체 조회하겠다는 의미
// C는 ord연산자 없어도 문자를 숫자로 인식하여 계산함
// value는 자리수만큼(* 10) 증가함
// 10진수, 2진수, 16진수 모두 변환 가능하다
```



* 파이썬 예시

```python
def atoi(strings):
    value = 0
    for i in range(len(strings)):
        c = strings[i]
        # 0~9
        if c >= '0' and c <= '9': 
        # ASCII 코드로 비교 가능함, 연산자 오버로딩
            digit = ord(c) - ord('0')   
            # c - ('0')은 안된다XX
            # ASCII 변환 위해 ord('0')
        else:
            break
        value = value * 10 + digit
        # value = value*10 + c                
        # value = value*10 + ord(c) - ord('0')
    return value

a = "123"
print(type(a))
print(a)
b = atoi(a)
print(type(b))
print(b)
```



* itoa구현하기
  * str 함수 사용하지 않기
  * 양의 정수 입력 받아 문자열로 변환
  * 입력값: 변환할 정수값 - 변환된 문자열 저장 문자배열
  * 반환값: 없음
  * 음수 고려사항

```python
def itoa(num):
    x = num # 몫
    y = 0 # 나머지
    arr = []
    while x:
        y = x % 10
        x = x // 10
        arr.append(chr(y+ord('0')))
        # 아스키 코드 출발점을 지정해주려고 ord(0)사용
    arr.reverse()
    strings = "".join(arr)
    return strings


x = 123
print(x,type(x))

str1 = itoa(x)
print(str1, type(str1))
```





#### 문자열 교체하기

---

> 변수에 기존 값을 보관하여 메모리를 이동시켜야 함

```python
str1 = "abc 1,2 ABC"
print(str1)

str1 = str1.replace("1,2","one,two")
print(str1)

# 본래는 문자열 - 리스트 변환
# 1,2 뒷 부분을 보관하고
# one, two를 변경한 후
# 보관한 값을 덧붙인 다음
# 리스트 -> 문자열 재변환 
```



## 패턴 매칭

* 알고리즘 종류
  * Brute-force [구현]
  * 카프-라빈 [X]
  * KMP [개념]
  * 보이어-무어 [개념]



#### Brute Force

---

* 본문 문자열을 처음부터 끝까지 순회하며 패턴 내 문자들을 일일이 비교하는 방식
  * t: TTTTAA, p: TTAT
  * i는 한 칸 이동(t) j는 처음부터 인덱싱(p)하여 비교

```python
p = "is" # 찾을 패턴
t = "This is a book~!" # 전체 텍스트
M = len(p) # 찾을 패턴 길이
N = len(t) # 전체 텍스트 길이

def BruteForce(p,t):
    i = 0 # t 인덱스
    j = 0 # p 인덱스
    while j < M and i < N:
        if t[i] != p[j]:
            i = i-j
            j = -1
        i = i + 1
        j = j + 1
    if j == M: return i-M # 검색 성공
                          # i-M이 패턴 시작점
    else: return -1 # 검색 실패
```



* 시간 복잡도
  * 최악의 경우 시간 복잡도는 모든 패턴 비교
  * O(MN) [N은전체 테스트 길이,M은 패턴 길이]



#### KMP알고리즘

---

* 불일치가 발생한 텍스트 스트링의 앞 부분에 어떤 문자가 있는지 미리 알고 있으므로 앞 부분에 대하여 다시 비교하지 않고 매칭을 수행

  * 패턴을 전처리, 배열 next[M]을 구하여 잘못된 시작 최소화
  * next[M] : 불일치 발생 경우 이동할 다음 위치
  * O(M+N)

  

* 아이디어 설명

  * 텍스트에서 abcdabc까지는 매치, e에서 실패한 상황

  * 패턴의 맨 앞의 abc와 실패 직전의 abc는 동일함을 이용할 수 있음

    * 테스트 : abcd abcd ...
    * pattern: abcd abcef

    

* 매칭이 실패했을 때 돌아갈 곳을 계산함

  * 패턴의 각 위치에 대해 실패 시 돌아갈 곳을 준비함

  * | a    | b    | c    | d    | a    | b    | c    | e    | f    |      |
    | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
    | -1   | 0    | 0    | 0    | 0    | 1    | 2    | 3    | 0    | 0    |

  * a bcd a

    * b자리에 1

  * ab cd ab

    * c 자리에 2

  * abc d abc

    * e 자리에 3

  * e와 매칭이 실패했고 돌아갈 곳의 계산 값은 3으로 문자 d의 위치를 의미한다



#### 보이어-무어 알고리즘

---

> 오른쪽에서 왼쪽으로 비교하는 알고리즘
>
> horspool

* 대부분 상용 소프트웨어에서 채택
* 오른쪽 끝에 있는 문자가 불일치하고
  이 문자가 패턴 내 존재하지 않는 경우, 이동 거리는 무려 패턴의 길이 만큼 된다
* 패턴 내 글자가 존재하는 경우 위치를 맞춘다
  
* 글자가 중복되는 경우 가장 끝 쪽에 위치한 글자와 일치시킨다
  
* rith 문자열의 skip 배열

  * | m    | h    | t    | i    | r    | 모든 문자 |
    | ---- | ---- | ---- | ---- | ---- | --------- |
    | 5    | 1    | 2    | 3    | 4    | 5         |



#### 매칭 알고리즘 비교

---

* 패턴 길이 m, 총 문자열 길이 n 일때
* Brute-force: O(mn)
* 카프-라빈 O(n) 최선n
* KMP O(n) 최선n
* 보이어 무어
  * 테스트 문자를 다 보지 않아도 된다
  * 최악은 O(mn)
  * 일반적으로는 O(n)보다 적게 듬





#### Pattern-Brute-force 연습문제

---

```python
def brute(t,p):
    i,j = 0,0
    while j < len(p) and i < len(t):
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == len(p):
        return i - len(p)
    else:
        return -1

test = "a pattern matching algorithm part 1"
pattern = "rithm"

N = len(test)
M = len(pattern)

i = 0
j = 0

while i < N and j < M:
    if test[i] != pattern[j]:
        i = i-j
        j = -1
    i += 1
    j += 1
if j == M:
    print(test[i-M:i])
else:
    print(-1)
```



### KMP코드

```python
def preprocess(P, M, PI):
    i,j = 0, -1
    PI[0] = -1
    while i < M:
        while j > -1 and P[i] != P[j]:
            j = PI[j]
        i += 1
        j += 1
        PI[i] = j
```

| a    | b    | c    | d    | a    | b    | c    | e    | f    |      | i    | j    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| -1   |      |      |      |      |      |      |      |      |      | 0    | -1   |
| -1   |      |      |      |      |      |      |      |      |      | 1    | 0    |
| -1   | 0    |      |      |      |      |      |      |      |      | 1    | -1   |
| -1   | 0    | 0    |      |      |      |      |      |      |      | 2    | 0    |
| -1   | 0    | 0    |      |      |      |      |      |      |      | 2    | -1   |
| -1   | 0    | 0    | 0    |      |      |      |      |      |      | 3    | 0    |
| -1   | 0    | 0    | 0    |      |      |      |      |      |      | 3    | -1   |
| -1   | 0    | 0    | 0    | 0    |      |      |      |      |      | 4    | 0    |
| -1   | 0    | 0    | 0    | 0    | 1    |      |      |      |      | 4    | 1    |
| -1   | 0    | 0    | 0    | 0    | 1    |      |      |      |      | 4    | -1   |
| -1   | 0    | 0    | 0    | 0    | 1    |      |      |      |      | 5    | 0    |
|      |      |      |      |      |      |      |      |      |      |      |      |
|      |      |      |      |      |      |      |      |      |      |      |      |

```python
def KMP(T,N,P,M,PI):
    i,j = 0,0
    pos = -1
    while i < N:
        while j >=0 and T[i] != P[j]:
            i = PI[j]
        i += 1
        j += 1
        if j == M:
            pos = i-j
            break
    return pos
```

```python
T = "a pattern matching algorithm part 1"
P = "rithm"
PI = [0] * (len(P) + 1)
N = len(T)
M = len(P)
prprocess(P,M,PI)
pos = KMP(T,N,P,M,PI)
print(pos)
```



### 보이어-무어

| m       | h      | t      | i      | r      | 모든 문자 |
| ------- | ------ | ------ | ------ | ------ | --------- |
| 5       | 1      | 2      | 3      | 4      | 5         |
| 0 [5-0] | 4[5-4] | 3[5-3] | 2[5-2] | 1[5-1] | 5         |

```python
def preprocess(P,M,PI):
    for i in range(M-1):
        PI[ord(P[i])] = i + 1 #m-1-i
        
def BoyerMooreHorspool(T,N,P,M,PI):
    i,j,k,l = 0,0,0,0
    pos = -1
    while i <= N-M:
        j = M-1
        k = i+M -1
        while j >= 0 and P[j] == T[k]:
            j -= 1
            k -= 1
        if j == -1:
            pos = i
            break
        i = i + (M-PI[ord(T(i+M-1))])

    return pos

T = "a pattern matching algorithm part 1"
P = "rithm"

ASCII = 128
PI = [0] * (ASCII+1)

N = len(T)
M - len(P)
preprocess(P,M,PI)
pos = BoyerMooreHorspool(T,N,P,M,PI)
print(pos)
```

