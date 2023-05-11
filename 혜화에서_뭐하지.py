## 최소 시간으로 원하는 장소 방문하는 코드 ##
## 클래스와 함수 선언 부분 ##
import itertools

class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]



    def getMinCostAndPath(self, start, end):
        visited = [False] * self.SIZE
        dist = [float('inf')] * self.SIZE
        dist[start] = 0
        prev = [None] * self.SIZE

        for _ in range(self.SIZE):
            min_distance = float('inf')
            for i in range(self.SIZE):
                if not visited[i] and dist[i] < min_distance:
                    min_distance = dist[i]
                    current = i

            visited[current] = True
            for neighbor in range(self.SIZE):
                if not visited[neighbor] and self.graph[current][neighbor] != 0:
                    new_distance = dist[current] + self.graph[current][neighbor]
                    if new_distance < dist[neighbor]:
                        dist[neighbor] = new_distance
                        prev[neighbor] = current

        path = []
        current = end
        while current != start:
            path.append(current)
            current = prev[current]
        path.append(start)
        path.reverse()

        return dist[end], path
    def getMinCostTour(self, nodes):
        min_cost = float('inf')
        min_path = []
        start = nodes[0]

        for permutation in itertools.permutations(nodes[1:]):
            path = [start] + list(permutation)
            total_cost = 0
            for i in range(len(path) - 1):
                cost, _ = self.getMinCostAndPath(path[i], path[i+1])
                total_cost += cost
            if total_cost < min_cost:
                min_cost = total_cost
                min_path = path

        return min_cost, min_path

def printGraph(g):
    print(' ', end=' ')
    for v in range(g.SIZE):
        print(nameAry[v], end=' ')
    print()
    for row in range(g.SIZE):
        print(nameAry[row], end=' ')
        for col in range(g.SIZE):
            print(g.graph[row][col], end=' ')
        print()
    print()


def findVertex(g, findVtx):  # 정점이 그래프에 연결되어 있는지 확인하는 함수
    stack = []
    visitedAry = []  # 방문한 정점

    current = 0  # 시작 정점
    stack.append(current)
    visitedAry.append(current)

    while (len(stack) != 0):
        next = None
        for vertex in range(gSize):
            if g.graph[current][vertex] != 0:
                if vertex in visitedAry:  # 방문한 적이 있는 정점이면 탈락
                    pass
                else:  # 방문한 적이 없으면 다음 정점으로 지정
                    next = vertex
                    break

        if next != None:  # 다음에 방문할 정점이 있는 경우
            current = next
            stack.append(current)
            visitedAry.append(current)
        else:  # 다음에 방문할 정점이 없는 경우
            current = stack.pop()

    if findVtx in visitedAry:
        return True
    else:
        return False

## 전역 변수 선언 부분 ##
G1 = None
nameAry = ['혜화역', '페르시안 궁전', '이삭토스트', '나누미떡볶이', '머노까머나', '뎁짜이', '호호식당','메밀향그집','정돈','군자대한곱창','칸다소바',\
           '순대실록','핏제리아오','투파인드피터','고부기','코야코',\
           '이디야_대학로점','삼원샏','학림','CONCRETE_PALETTE','스타벅스_혜화역점','스타벅스_마로니에공원점','스타벅스_동숭로아트점',\
           '링크아트센터', '서연아트홀','쿼드','예스24스테이지','컬쳐씨어터','자유극장','티오엠','드림씨어터',\
           '국립어린이과학관','짚풀박물관','아르코미술관','낙산공원']

#혜화역 변수
혜화역 = 0
#음식점 변수
페르시안궁전, 이삭토스트, 나누미떡볶이, 머노까머나, 뎁짜이, 호호식당, 메밀향그집, 정돈, 군자대한곱창, 칸다소바 =  1, 2, 3, 4, 5, 6, 7, 8, 9, 10
순대실록, 핏제리아오, 투파인드피터, 고부기, 코야코 = 11, 12, 13, 14, 15
#카페 변수
이디야_대학로점, 삼원샏, 학림, CONCRETE_PALETTE, 스타벅스_혜화역점, 스타벅스_마로니에공원점, 스타벅스_동숭로아트점 = 16, 17, 18, 19, 20, 21, 22
#연극 변수
링크아트센터, 서연아트홀, 쿼드, 예스24스테이지, 컬쳐씨어터, 자유극장, 티오엠, 드림씨어터 = 23, 24, 25, 26, 27, 28, 29, 30
#놀거리 변수
국립어린이과학관, 짚풀박물관, 아르코미술관, 낙산공원 = 31, 32, 33, 34

## 그래프 구성 코드 부분 ##
gSize = 35
G1 = Graph(gSize)

# 혜화역 -> 음식점
G1.graph[혜화역][페르시안궁전] = 9
G1.graph[혜화역][이삭토스트] = 8
G1.graph[혜화역][나누미떡볶이] = 7
G1.graph[혜화역][머노까머나] = 4
G1.graph[혜화역][뎁짜이] = 4
G1.graph[혜화역][호호식당] = 5
G1.graph[혜화역][메밀향그집] = 3
G1.graph[혜화역][정돈] = 1
G1.graph[혜화역][군자대한곱창] = 1
G1.graph[혜화역][칸다소바] = 2
G1.graph[혜화역][순대실록] = 2
G1.graph[혜화역][핏제리아오] = 5
G1.graph[혜화역][투파인드피터] = 2
G1.graph[혜화역][고부기] = 4
G1.graph[혜화역][코야코] = 4


# 음식점 -> 혜화역
G1.graph[페르시안궁전][혜화역] = 9
G1.graph[이삭토스트][혜화역] = 8
G1.graph[나누미떡볶이][혜화역] = 7
G1.graph[머노까머나][혜화역] = 4
G1.graph[뎁짜이][혜화역] = 4
G1.graph[호호식당][혜화역] = 3
G1.graph[메밀향그집][혜화역] = 3
G1.graph[정돈][혜화역] = 1
G1.graph[군자대한곱창][혜화역] = 1
G1.graph[칸다소바][혜화역] = 2
G1.graph[순대실록][혜화역] = 2
G1.graph[핏제리아오][혜화역] = 5
G1.graph[투파인드피터][혜화역] = 2
G1.graph[고부기][혜화역] = 4
G1.graph[코야코][혜화역] = 4


#혜화역 -> 카페
G1.graph[혜화역][이디야_대학로점] = 4
G1.graph[혜화역][삼원샏] = 5
G1.graph[혜화역][학림] = 3
G1.graph[혜화역][CONCRETE_PALETTE] = 4
G1.graph[혜화역][스타벅스_혜화역점] = 3
G1.graph[혜화역][스타벅스_마로니에공원점] = 2
G1.graph[혜화역][스타벅스_동숭로아트점] = 6


## 카페 -> 혜화역
G1.graph[이디야_대학로점][혜화역] = 4
G1.graph[삼원샏][혜화역] = 5
G1.graph[학림][혜화역] = 3
G1.graph[CONCRETE_PALETTE][혜화역] = 4
G1.graph[스타벅스_혜화역점][혜화역] = 3
G1.graph[스타벅스_마로니에공원점][혜화역] = 2
G1.graph[스타벅스_동숭로아트점][혜화역] = 6


## 혜화역 -> 극장
G1.graph[혜화역][링크아트센터] = 5
G1.graph[혜화역][서연아트홀] = 5
G1.graph[혜화역][쿼드] = 5
G1.graph[혜화역][예스24스테이지] = 4
G1.graph[혜화역][컬쳐씨어터] = 5
G1.graph[혜화역][자유극장] = 5
G1.graph[혜화역][티오엠] = 5
G1.graph[혜화역][드림씨어터] = 4

## 극장 -> 혜화역
G1.graph[링크아트센터][혜화역] = 5
G1.graph[서연아트홀][혜화역] = 5
G1.graph[쿼드][혜화역] = 5
G1.graph[예스24스테이지][혜화역] = 4
G1.graph[컬쳐씨어터][혜화역] = 5
G1.graph[자유극장][혜화역] = 5
G1.graph[티오엠][혜화역] = 5
G1.graph[드림씨어터][혜화역] = 4


##혜화역 -> 놀거리
G1.graph[혜화역][국립어린이과학관] = 13
G1.graph[혜화역][짚풀박물관] = 9
G1.graph[혜화역][아르코미술관] = 4
G1.graph[혜화역][낙산공원] = 11


##놀거리 -> 혜화역
G1.graph[국립어린이과학관][혜화역] = 13
G1.graph[짚풀박물관][혜화역] = 9
G1.graph[아르코미술관][혜화역] = 4
G1.graph[낙산공원][혜화역] = 11


## 카페 -> 놀거리
G1.graph[이디야_대학로점][국립어린이과학관] = 19
G1.graph[이디야_대학로점][짚풀박물관] = 11
G1.graph[이디야_대학로점][아르코미술관] = 3
G1.graph[이디야_대학로점][낙산공원] = 9

G1.graph[삼원샏][국립어린이과학관] = 10
G1.graph[삼원샏][짚풀박물관] = 9
G1.graph[삼원샏][아르코미술관] = 7
G1.graph[삼원샏][낙산공원] = 13

G1.graph[학림][국립어린이과학관] = 16
G1.graph[학림][짚풀박물관] = 8
G1.graph[학림][아르코미술관] = 5
G1.graph[학림][낙산공원] = 12

G1.graph[CONCRETE_PALETTE][국립어린이과학관] = 15
G1.graph[CONCRETE_PALETTE][짚풀박물관] = 7
G1.graph[CONCRETE_PALETTE][아르코미술관] = 6
G1.graph[CONCRETE_PALETTE][낙산공원] = 13

G1.graph[스타벅스_혜화역점][국립어린이과학관] = 16
G1.graph[스타벅스_혜화역점][짚풀박물관] = 8
G1.graph[스타벅스_혜화역점][아르코미술관] = 5
G1.graph[스타벅스_혜화역점][낙산공원] = 12

G1.graph[스타벅스_마로니에공원점][국립어린이과학관] = 17
G1.graph[스타벅스_마로니에공원점][짚풀박물관] = 10
G1.graph[스타벅스_마로니에공원점][아르코미술관] = 3
G1.graph[스타벅스_마로니에공원점][낙산공원] = 10

G1.graph[스타벅스_동숭로아트점][국립어린이과학관] = 18
G1.graph[스타벅스_동숭로아트점][짚풀박물관] = 10
G1.graph[스타벅스_동숭로아트점][아르코미술관] = 5
G1.graph[스타벅스_동숭로아트점][낙산공원] = 10


## 놀거리 -> 카페
G1.graph[국립어린이과학관][이디야_대학로점] = 19
G1.graph[짚풀박물관][이디야_대학로점] = 11
G1.graph[아르코미술관][이디야_대학로점] = 3
G1.graph[낙산공원][이디야_대학로점] = 9

G1.graph[국립어린이과학관][삼원샏] = 10
G1.graph[짚풀박물관][삼원샏] = 9
G1.graph[아르코미술관][삼원샏] = 7
G1.graph[낙산공원][삼원샏] = 13

G1.graph[국립어린이과학관][학림] = 16
G1.graph[짚풀박물관][학림] = 8
G1.graph[아르코미술관][학림] = 5
G1.graph[낙산공원][학림] = 12

G1.graph[국립어린이과학관][CONCRETE_PALETTE] = 15
G1.graph[짚풀박물관][CONCRETE_PALETTE] = 7
G1.graph[아르코미술관][CONCRETE_PALETTE] = 6
G1.graph[낙산공원][CONCRETE_PALETTE] = 13

G1.graph[국립어린이과학관][스타벅스_혜화역점] = 16
G1.graph[짚풀박물관][스타벅스_혜화역점] = 8
G1.graph[아르코미술관][스타벅스_혜화역점] = 5
G1.graph[낙산공원][스타벅스_혜화역점] = 12

G1.graph[국립어린이과학관][스타벅스_마로니에공원점] = 17
G1.graph[짚풀박물관][스타벅스_마로니에공원점] = 10
G1.graph[아르코미술관][스타벅스_마로니에공원점] = 3
G1.graph[낙산공원][스타벅스_마로니에공원점] = 9

G1.graph[국립어린이과학관][스타벅스_동숭로아트점] = 18
G1.graph[짚풀박물관][스타벅스_동숭로아트점] = 10
G1.graph[아르코미술관][스타벅스_동숭로아트점] = 5
G1.graph[낙산공원][스타벅스_동숭로아트점] = 10


# 연극 -> 카페
G1.graph[링크아트센터][이디야_대학로점] = 8
G1.graph[서연아트홀][이디야_대학로점] = 8
G1.graph[쿼드][이디야_대학로점] = 5
G1.graph[예스24스테이지][이디야_대학로점] = 3
G1.graph[컬쳐씨어터][이디야_대학로점] = 2
G1.graph[자유극장][이디야_대학로점] = 3
G1.graph[티오엠][이디야_대학로점] = 2
G1.graph[드림씨어터][이디야_대학로점] = 2

G1.graph[링크아트센터][삼원샏] = 7
G1.graph[서연아트홀][삼원샏] = 5
G1.graph[쿼드][삼원샏] = 7
G1.graph[예스24스테이지][삼원샏] = 6
G1.graph[컬쳐씨어터][삼원샏] = 6
G1.graph[자유극장][삼원샏] = 6
G1.graph[티오엠][삼원샏] = 6
G1.graph[드림씨어터][삼원샏] = 6

G1.graph[링크아트센터][학림] = 7
G1.graph[서연아트홀][학림] = 4 
G1.graph[쿼드][학림] = 6
G1.graph[예스24스테이지][학림] = 4
G1.graph[컬쳐씨어터][학림] = 4
G1.graph[자유극장][학림] = 5
G1.graph[티오엠][학림] = 4
G1.graph[드림씨어터][학림] = 3

G1.graph[링크아트센터][CONCRETE_PALETTE] = 6
G1.graph[서연아트홀][CONCRETE_PALETTE] = 4
G1.graph[쿼드][CONCRETE_PALETTE] = 5
G1.graph[예스24스테이지][CONCRETE_PALETTE] = 4
G1.graph[컬쳐씨어터][CONCRETE_PALETTE] = 4
G1.graph[자유극장][CONCRETE_PALETTE] = 5
G1.graph[티오엠][CONCRETE_PALETTE] = 5
G1.graph[드림씨어터][CONCRETE_PALETTE] = 4

G1.graph[링크아트센터][스타벅스_혜화역점] = 6
G1.graph[서연아트홀][스타벅스_혜화역점] = 9
G1.graph[쿼드][스타벅스_혜화역점] = 5
G1.graph[예스24스테이지][스타벅스_혜화역점] = 3
G1.graph[컬쳐씨어터][스타벅스_혜화역점] = 4
G1.graph[자유극장][스타벅스_혜화역점] = 4
G1.graph[티오엠][스타벅스_혜화역점] = 4
G1.graph[드림씨어터][스타벅스_혜화역점] = 4

G1.graph[링크아트센터][스타벅스_마로니에공원점] = 7
G1.graph[서연아트홀][스타벅스_마로니에공원점] = 7
G1.graph[쿼드][스타벅스_마로니에공원점] = 6
G1.graph[예스24스테이지][스타벅스_마로니에공원점] = 4
G1.graph[컬쳐씨어터][스타벅스_마로니에공원점] = 4
G1.graph[자유극장][스타벅스_마로니에공원점] = 5
G1.graph[티오엠][스타벅스_마로니에공원점] = 3
G1.graph[드림씨어터][스타벅스_마로니에공원점] = 3

G1.graph[링크아트센터][스타벅스_동숭로아트점] = 5
G1.graph[서연아트홀][스타벅스_동숭로아트점] = 8
G1.graph[쿼드][스타벅스_동숭로아트점] = 2
G1.graph[예스24스테이지][스타벅스_동숭로아트점] = 2
G1.graph[컬쳐씨어터][스타벅스_동숭로아트점] = 2
G1.graph[자유극장][스타벅스_동숭로아트점] = 1
G1.graph[티오엠][스타벅스_동숭로아트점] = 2
G1.graph[드림씨어터][스타벅스_동숭로아트점] = 2


## 카페 -> 연극
G1.graph[이디야_대학로점][링크아트센터] = 8
G1.graph[이디야_대학로점][서연아트홀] = 8
G1.graph[이디야_대학로점][쿼드] = 5
G1.graph[이디야_대학로점][예스24스테이지] = 3
G1.graph[이디야_대학로점][컬쳐씨어터] = 2
G1.graph[이디야_대학로점][자유극장] = 3
G1.graph[이디야_대학로점][티오엠] = 2
G1.graph[이디야_대학로점][드림씨어터] = 2

G1.graph[삼원샏][링크아트센터] = 7
G1.graph[삼원샏][서연아트홀] = 5
G1.graph[삼원샏][쿼드] = 7
G1.graph[삼원샏][예스24스테이지] = 6
G1.graph[삼원샏][컬쳐씨어터] = 6
G1.graph[삼원샏][자유극장] = 6
G1.graph[삼원샏][티오엠] = 6
G1.graph[삼원샏][드림씨어터] = 6

G1.graph[학림][링크아트센터] = 7
G1.graph[학림][서연아트홀] = 4 
G1.graph[학림][쿼드] = 6
G1.graph[학림][예스24스테이지] = 4
G1.graph[학림][컬쳐씨어터] = 4
G1.graph[학림][자유극장] = 5
G1.graph[학림][티오엠] = 4
G1.graph[학림][드림씨어터] = 3

G1.graph[CONCRETE_PALETTE][링크아트센터] = 6
G1.graph[CONCRETE_PALETTE][서연아트홀] = 4
G1.graph[CONCRETE_PALETTE][쿼드] = 5
G1.graph[CONCRETE_PALETTE][예스24스테이지] = 4
G1.graph[CONCRETE_PALETTE][컬쳐씨어터] = 4
G1.graph[CONCRETE_PALETTE][자유극장] = 5
G1.graph[CONCRETE_PALETTE][티오엠] = 5
G1.graph[CONCRETE_PALETTE][드림씨어터] = 4

G1.graph[스타벅스_혜화역점][링크아트센터] = 6
G1.graph[스타벅스_혜화역점][서연아트홀] = 9
G1.graph[스타벅스_혜화역점][쿼드] = 5
G1.graph[스타벅스_혜화역점][예스24스테이지] = 3
G1.graph[스타벅스_혜화역점][컬쳐씨어터] = 4
G1.graph[스타벅스_혜화역점][자유극장] = 4
G1.graph[스타벅스_혜화역점][티오엠] = 4
G1.graph[스타벅스_혜화역점][드림씨어터] = 4

G1.graph[스타벅스_마로니에공원점][링크아트센터] = 7
G1.graph[스타벅스_마로니에공원점][서연아트홀] = 7
G1.graph[스타벅스_마로니에공원점][쿼드] = 6
G1.graph[스타벅스_마로니에공원점][예스24스테이지] = 4
G1.graph[스타벅스_마로니에공원점][컬쳐씨어터] = 4
G1.graph[스타벅스_마로니에공원점][자유극장] = 5
G1.graph[스타벅스_마로니에공원점][티오엠] = 3
G1.graph[스타벅스_마로니에공원점][드림씨어터] = 3

G1.graph[스타벅스_동숭로아트점][링크아트센터] = 5
G1.graph[스타벅스_동숭로아트점][서연아트홀] = 8
G1.graph[스타벅스_동숭로아트점][쿼드] = 2
G1.graph[스타벅스_동숭로아트점][예스24스테이지] = 2
G1.graph[스타벅스_동숭로아트점][컬쳐씨어터] = 2
G1.graph[스타벅스_동숭로아트점][자유극장] = 1
G1.graph[스타벅스_동숭로아트점][티오엠] = 2
G1.graph[스타벅스_동숭로아트점][드림씨어터] = 2


# 음식점 -> 카페
G1.graph[페르시안궁전][이디야_대학로점] = 13
G1.graph[페르시안궁전][삼원샏] = 9
G1.graph[페르시안궁전][학림] = 10
G1.graph[페르시안궁전][CONCRETE_PALETTE] = 9
G1.graph[페르시안궁전][스타벅스_혜화역점] = 12
G1.graph[페르시안궁전][스타벅스_마로니에공원점] = 12
G1.graph[페르시안궁전][스타벅스_동숭로아트점] = 13

G1.graph[이삭토스트][이디야_대학로점] = 12
G1.graph[이삭토스트][삼원샏] = 8
G1.graph[이삭토스트][학림] = 9
G1.graph[이삭토스트][CONCRETE_PALETTE] = 8
G1.graph[이삭토스트][스타벅스_혜화역점] = 10
G1.graph[이삭토스트][스타벅스_마로니에공원점] = 11
G1.graph[이삭토스트][스타벅스_동숭로아트점] = 12

G1.graph[나누미떡볶이][이디야_대학로점] = 11
G1.graph[나누미떡볶이][삼원샏] = 7
G1.graph[나누미떡볶이][학림] = 8
G1.graph[나누미떡볶이][CONCRETE_PALETTE] = 7
G1.graph[나누미떡볶이][스타벅스_혜화역점] = 9
G1.graph[나누미떡볶이][스타벅스_마로니에공원점] = 10
G1.graph[나누미떡볶이][스타벅스_동숭로아트점] = 11

G1.graph[머노까머나][이디야_대학로점] = 8
G1.graph[머노까머나][삼원샏] = 4
G1.graph[머노까머나][학림] = 5
G1.graph[머노까머나][CONCRETE_PALETTE] = 5
G1.graph[머노까머나][스타벅스_혜화역점] = 7
G1.graph[머노까머나][스타벅스_마로니에공원점] = 7
G1.graph[머노까머나][스타벅스_동숭로아트점] = 9

G1.graph[뎁짜이][이디야_대학로점] = 7
G1.graph[뎁짜이][삼원샏] = 3
G1.graph[뎁짜이][학림] = 4
G1.graph[뎁짜이][CONCRETE_PALETTE] = 3
G1.graph[뎁짜이][스타벅스_혜화역점] = 6
G1.graph[뎁짜이][스타벅스_마로니에공원점] = 6
G1.graph[뎁짜이][스타벅스_동숭로아트점] = 8

G1.graph[호호식당][이디야_대학로점] = 6
G1.graph[호호식당][삼원샏] = 2
G1.graph[호호식당][학림] = 3
G1.graph[호호식당][CONCRETE_PALETTE] = 3
G1.graph[호호식당][스타벅스_혜화역점] = 5
G1.graph[호호식당][스타벅스_마로니에공원점] = 5
G1.graph[호호식당][스타벅스_동숭로아트점] = 8

G1.graph[메밀향그집][이디야_대학로점] = 5
G1.graph[메밀향그집][삼원샏] = 1
G1.graph[메밀향그집][학림] = 2
G1.graph[메밀향그집][CONCRETE_PALETTE] = 2
G1.graph[메밀향그집][스타벅스_혜화역점] = 4
G1.graph[메밀향그집][스타벅스_마로니에공원점] = 4
G1.graph[메밀향그집][스타벅스_동숭로아트점] = 7

G1.graph[정돈][이디야_대학로점] = 4
G1.graph[정돈][삼원샏] = 3
G1.graph[정돈][학림] = 1
G1.graph[정돈][CONCRETE_PALETTE] = 2
G1.graph[정돈][스타벅스_혜화역점] = 3
G1.graph[정돈][스타벅스_마로니에공원점] = 3
G1.graph[정돈][스타벅스_동숭로아트점] = 6

G1.graph[군자대한곱창][이디야_대학로점] = 6
G1.graph[군자대한곱창][삼원샏] = 2
G1.graph[군자대한곱창][학림] = 3
G1.graph[군자대한곱창][CONCRETE_PALETTE] = 2
G1.graph[군자대한곱창][스타벅스_혜화역점] = 3
G1.graph[군자대한곱창][스타벅스_마로니에공원점] = 5 
G1.graph[군자대한곱창][스타벅스_동숭로아트점] = 6

G1.graph[칸다소바][이디야_대학로점] = 4
G1.graph[칸다소바][삼원샏] = 2
G1.graph[칸다소바][학림] = 2
G1.graph[칸다소바][CONCRETE_PALETTE] = 1
G1.graph[칸다소바][스타벅스_혜화역점] = 2
G1.graph[칸다소바][스타벅스_마로니에공원점] = 3
G1.graph[칸다소바][스타벅스_동숭로아트점] = 5

G1.graph[순대실록][이디야_대학로점] = 4
G1.graph[순대실록][삼원샏] = 5
G1.graph[순대실록][학림] = 5
G1.graph[순대실록][CONCRETE_PALETTE] = 4
G1.graph[순대실록][스타벅스_혜화역점] = 3
G1.graph[순대실록][스타벅스_마로니에공원점] = 5 
G1.graph[순대실록][스타벅스_동숭로아트점] = 4

G1.graph[핏제리아오][이디야_대학로점] = 4
G1.graph[핏제리아오][삼원샏] = 8 
G1.graph[핏제리아오][학림] = 6
G1.graph[핏제리아오][CONCRETE_PALETTE] = 7
G1.graph[핏제리아오][스타벅스_혜화역점] = 4
G1.graph[핏제리아오][스타벅스_마로니에공원점] = 6
G1.graph[핏제리아오][스타벅스_동숭로아트점] = 2

G1.graph[투파인드피터][이디야_대학로점] = 1
G1.graph[투파인드피터][삼원샏] = 5
G1.graph[투파인드피터][학림] = 3
G1.graph[투파인드피터][CONCRETE_PALETTE] = 4
G1.graph[투파인드피터][스타벅스_혜화역점] = 3
G1.graph[투파인드피터][스타벅스_마로니에공원점] = 2
G1.graph[투파인드피터][스타벅스_동숭로아트점] = 2 

G1.graph[고부기][이디야_대학로점] = 4
G1.graph[고부기][삼원샏] = 8
G1.graph[고부기][학림] = 6
G1.graph[고부기][CONCRETE_PALETTE] = 7
G1.graph[고부기][스타벅스_혜화역점] = 5
G1.graph[고부기][스타벅스_마로니에공원점] = 4
G1.graph[고부기][스타벅스_동숭로아트점] = 3

G1.graph[코야코][이디야_대학로점] = 4
G1.graph[코야코][삼원샏] = 8 
G1.graph[코야코][학림] = 6
G1.graph[코야코][CONCRETE_PALETTE] = 7
G1.graph[코야코][스타벅스_혜화역점] = 5
G1.graph[코야코][스타벅스_마로니에공원점] = 4 
G1.graph[코야코][스타벅스_동숭로아트점] = 3

#연극->음식점
G1.graph[링크아트센터][페르시안궁전] = 13
G1.graph[링크아트센터][이삭토스트] = 12
G1.graph[링크아트센터][나누미떡볶이] = 11
G1.graph[링크아트센터][머노까머나] = 8
G1.graph[링크아트센터][뎁짜이] = 8
G1.graph[링크아트센터][호호식당] = 8
G1.graph[링크아트센터][메밀향그집] = 7
G1.graph[링크아트센터][정돈] = 8
G1.graph[링크아트센터][군자대한곱창] = 5
G1.graph[링크아트센터][칸다소바] = 5
G1.graph[링크아트센터][순대실록] = 3
G1.graph[링크아트센터][핏제리아오] = 7
G1.graph[링크아트센터][투파인드피터] = 6
G1.graph[링크아트센터][고부기] = 7
G1.graph[링크아트센터][코야코] = 7

G1.graph[서연아트홀][페르시안궁전] = 7
G1.graph[서연아트홀][이삭토스트] = 7
G1.graph[서연아트홀][나누미떡볶이] = 6
G1.graph[서연아트홀][머노까머나] = 4
G1.graph[서연아트홀][뎁짜이] = 4
G1.graph[서연아트홀][호호식당] = 4
G1.graph[서연아트홀][메밀향그집] = 3
G1.graph[서연아트홀][정돈] = 6
G1.graph[서연아트홀][군자대한곱창] = 1
G1.graph[서연아트홀][칸다소바] = 3
G1.graph[서연아트홀][순대실록] = 6
G1.graph[서연아트홀][핏제리아오] = 9
G1.graph[서연아트홀][투파인드피터] = 8
G1.graph[서연아트홀][고부기] = 10
G1.graph[서연아트홀][코야코] = 10

G1.graph[쿼드][페르시안궁전] = 14
G1.graph[쿼드][이삭토스트] = 13
G1.graph[쿼드][나누미떡볶이] = 12
G1.graph[쿼드][머노까머나] = 8
G1.graph[쿼드][뎁짜이] = 8
G1.graph[쿼드][호호식당] = 8
G1.graph[쿼드][메밀향그집] = 6
G1.graph[쿼드][정돈] = 7
G1.graph[쿼드][군자대한곱창] = 6
G1.graph[쿼드][칸다소바] = 4
G1.graph[쿼드][순대실록] = 1
G1.graph[쿼드][핏제리아오] = 3
G1.graph[쿼드][투파인드피터] = 3
G1.graph[쿼드][고부기] = 4
G1.graph[쿼드][코야코] = 4

G1.graph[예스24스테이지][페르시안궁전] = 14
G1.graph[예스24스테이지][이삭토스트] = 13
G1.graph[예스24스테이지][나누미떡볶이] = 12
G1.graph[예스24스테이지][머노까머나] = 9
G1.graph[예스24스테이지][뎁짜이] = 7
G1.graph[예스24스테이지][호호식당] = 7
G1.graph[예스24스테이지][메밀향그집] = 6
G1.graph[예스24스테이지][정돈] = 6
G1.graph[예스24스테이지][군자대한곱창] = 5
G1.graph[예스24스테이지][칸다소바] = 4
G1.graph[예스24스테이지][순대실록] = 1
G1.graph[예스24스테이지][핏제리아오] = 3
G1.graph[예스24스테이지][투파인드피터] = 2
G1.graph[예스24스테이지][고부기] = 4
G1.graph[예스24스테이지][코야코] = 4

G1.graph[컬쳐씨어터][페르시안궁전] = 14
G1.graph[컬쳐씨어터][이삭토스트] = 13
G1.graph[컬쳐씨어터][나누미떡볶이] = 12
G1.graph[컬쳐씨어터][머노까머나] = 9
G1.graph[컬쳐씨어터][뎁짜이] = 8
G1.graph[컬쳐씨어터][호호식당] = 7
G1.graph[컬쳐씨어터][메밀향그집] = 6
G1.graph[컬쳐씨어터][정돈] = 6
G1.graph[컬쳐씨어터][군자대한곱창] = 5
G1.graph[컬쳐씨어터][칸다소바] = 4
G1.graph[컬쳐씨어터][순대실록] = 2
G1.graph[컬쳐씨어터][핏제리아오] = 3
G1.graph[컬쳐씨어터][투파인드피터] = 2
G1.graph[컬쳐씨어터][고부기] = 4
G1.graph[컬쳐씨어터][코야코] = 4

G1.graph[자유극장][페르시안궁전] = 15
G1.graph[자유극장][이삭토스트] = 14
G1.graph[자유극장][나누미떡볶이] = 13
G1.graph[자유극장][머노까머나] = 9
G1.graph[자유극장][뎁짜이] = 8
G1.graph[자유극장][호호식당] = 8
G1.graph[자유극장][메밀향그집] = 6
G1.graph[자유극장][정돈] = 6
G1.graph[자유극장][군자대한곱창] = 6
G1.graph[자유극장][칸다소바] = 5
G1.graph[자유극장][순대실록] = 2
G1.graph[자유극장][핏제리아오] = 2
G1.graph[자유극장][투파인드피터] = 2
G1.graph[자유극장][고부기] = 3
G1.graph[자유극장][코야코] = 3

G1.graph[티오엠][페르시안궁전] = 15
G1.graph[티오엠][이삭토스트] = 14
G1.graph[티오엠][나누미떡볶이] = 13
G1.graph[티오엠][머노까머나] = 10
G1.graph[티오엠][뎁짜이] = 8
G1.graph[티오엠][호호식당] = 7
G1.graph[티오엠][메밀향그집] = 6
G1.graph[티오엠][정돈] = 6
G1.graph[티오엠][군자대한곱창] = 6
G1.graph[티오엠][칸다소바] = 5
G1.graph[티오엠][순대실록] = 2
G1.graph[티오엠][핏제리아오] = 3
G1.graph[티오엠][투파인드피터] = 1
G1.graph[티오엠][고부기] = 4
G1.graph[티오엠][코야코] = 4

G1.graph[드림씨어터][페르시안궁전] = 14
G1.graph[드림씨어터][이삭토스트] = 13
G1.graph[드림씨어터][나누미떡볶이] = 12
G1.graph[드림씨어터][머노까머나] = 9
G1.graph[드림씨어터][뎁짜이] = 8
G1.graph[드림씨어터][호호식당] = 7
G1.graph[드림씨어터][메밀향그집] = 6
G1.graph[드림씨어터][정돈] = 5
G1.graph[드림씨어터][군자대한곱창] = 5
G1.graph[드림씨어터][칸다소바] = 4
G1.graph[드림씨어터][순대실록] = 3
G1.graph[드림씨어터][핏제리아오] = 4
G1.graph[드림씨어터][투파인드피터] = 2
G1.graph[드림씨어터][고부기] = 5
G1.graph[드림씨어터][코야코] = 5

#음식점->연극
G1.graph[페르시안궁전][링크아트센터] = 13
G1.graph[이삭토스트][링크아트센터] = 12
G1.graph[나누미떡볶이][링크아트센터] = 11
G1.graph[머노까머나][링크아트센터] = 8
G1.graph[뎁짜이][링크아트센터] = 8
G1.graph[호호식당][링크아트센터] = 8
G1.graph[메밀향그집][링크아트센터] = 7
G1.graph[정돈][링크아트센터] = 8
G1.graph[군자대한곱창][링크아트센터] = 5
G1.graph[칸다소바][링크아트센터] = 5
G1.graph[순대실록][링크아트센터] = 3
G1.graph[핏제리아오][링크아트센터] = 7
G1.graph[투파인드피터][링크아트센터] = 6
G1.graph[고부기][링크아트센터] = 7
G1.graph[코야코][링크아트센터] = 7

G1.graph[페르시안궁전][서연아트홀] = 7
G1.graph[이삭토스트][서연아트홀] = 7
G1.graph[나누미떡볶이][서연아트홀] = 6
G1.graph[머노까머나][서연아트홀] = 4
G1.graph[뎁짜이][서연아트홀] = 4
G1.graph[호호식당][서연아트홀] = 4
G1.graph[메밀향그집][서연아트홀] = 3
G1.graph[정돈][서연아트홀] = 6
G1.graph[군자대한곱창][서연아트홀] = 1
G1.graph[칸다소바][서연아트홀] = 3
G1.graph[순대실록][서연아트홀] = 6
G1.graph[핏제리아오][서연아트홀] = 9
G1.graph[투파인드피터][서연아트홀] = 8
G1.graph[고부기][서연아트홀] = 10
G1.graph[코야코][서연아트홀] = 10

G1.graph[페르시안궁전][쿼드] = 14
G1.graph[이삭토스트][쿼드] = 13
G1.graph[나누미떡볶이][쿼드] = 12
G1.graph[머노까머나][쿼드] = 8
G1.graph[뎁짜이][쿼드] = 8
G1.graph[호호식당][쿼드] = 8
G1.graph[메밀향그집][쿼드] = 6
G1.graph[정돈][쿼드] = 7
G1.graph[군자대한곱창][쿼드] = 6
G1.graph[칸다소바][쿼드] = 4
G1.graph[순대실록][쿼드] = 1
G1.graph[핏제리아오][쿼드] = 3
G1.graph[투파인드피터][쿼드] = 3
G1.graph[고부기][쿼드] = 4
G1.graph[코야코][쿼드] = 4

G1.graph[페르시안궁전][예스24스테이지] = 14
G1.graph[이삭토스트][예스24스테이지] = 13
G1.graph[나누미떡볶이][예스24스테이지] = 12
G1.graph[머노까머나][예스24스테이지] = 9
G1.graph[뎁짜이][예스24스테이지] = 7
G1.graph[호호식당][예스24스테이지] = 7
G1.graph[메밀향그집][예스24스테이지] = 6
G1.graph[정돈][예스24스테이지] = 6
G1.graph[군자대한곱창][예스24스테이지] = 5
G1.graph[칸다소바][예스24스테이지] = 4
G1.graph[순대실록][예스24스테이지] = 1
G1.graph[핏제리아오][예스24스테이지] = 3
G1.graph[투파인드피터][예스24스테이지] = 2
G1.graph[고부기][예스24스테이지] = 4
G1.graph[코야코][예스24스테이지] = 4

G1.graph[페르시안궁전][컬쳐씨어터] = 14
G1.graph[이삭토스트][컬쳐씨어터] = 13
G1.graph[나누미떡볶이][컬쳐씨어터] = 12
G1.graph[머노까머나][컬쳐씨어터] = 9
G1.graph[뎁짜이][컬쳐씨어터] = 8
G1.graph[호호식당][컬쳐씨어터] = 7
G1.graph[메밀향그집][컬쳐씨어터] = 6
G1.graph[정돈][컬쳐씨어터] = 6
G1.graph[군자대한곱창][컬쳐씨어터] = 5
G1.graph[칸다소바][컬쳐씨어터] = 4
G1.graph[순대실록][컬쳐씨어터] = 2
G1.graph[핏제리아오][컬쳐씨어터] = 3
G1.graph[투파인드피터][컬쳐씨어터] = 2
G1.graph[고부기][컬쳐씨어터] = 4
G1.graph[코야코][컬쳐씨어터] = 4

G1.graph[페르시안궁전][자유극장] = 15
G1.graph[이삭토스트][자유극장] = 14
G1.graph[나누미떡볶이][자유극장] = 13
G1.graph[머노까머나][자유극장] = 9
G1.graph[뎁짜이][자유극장] = 8
G1.graph[호호식당][자유극장] = 8
G1.graph[메밀향그집][자유극장] = 6
G1.graph[정돈][자유극장] = 6
G1.graph[군자대한곱창][자유극장] = 6
G1.graph[칸다소바][자유극장] = 5
G1.graph[순대실록][자유극장] = 2
G1.graph[핏제리아오][자유극장] = 2
G1.graph[투파인드피터][자유극장] = 2
G1.graph[고부기][자유극장] = 3
G1.graph[코야코] [자유극장]= 3

G1.graph[페르시안궁전][티오엠] = 15
G1.graph[이삭토스트][티오엠] = 14
G1.graph[나누미떡볶이][티오엠] = 13
G1.graph[머노까머나][티오엠] = 10
G1.graph[뎁짜이][티오엠] = 8
G1.graph[호호식당][티오엠] = 7
G1.graph[메밀향그집][티오엠] = 6
G1.graph[정돈][티오엠] = 6
G1.graph[군자대한곱창][티오엠] = 6
G1.graph[칸다소바][티오엠] = 5
G1.graph[순대실록][티오엠] = 2
G1.graph[핏제리아오][티오엠] = 3
G1.graph[투파인드피터][티오엠] = 1
G1.graph[고부기][티오엠] = 4
G1.graph[코야코][티오엠] = 4

G1.graph[페르시안궁전][드림씨어터] = 14
G1.graph[이삭토스트][드림씨어터] = 13
G1.graph[나누미떡볶이][드림씨어터] = 12
G1.graph[머노까머나][드림씨어터] = 9
G1.graph[뎁짜이][드림씨어터] = 8
G1.graph[호호식당][드림씨어터] = 7
G1.graph[메밀향그집][드림씨어터] = 6
G1.graph[정돈][드림씨어터] = 5
G1.graph[군자대한곱창][드림씨어터] = 5
G1.graph[칸다소바][드림씨어터] = 4
G1.graph[순대실록][드림씨어터] = 3
G1.graph[핏제리아오][드림씨어터] = 4
G1.graph[투파인드피터][드림씨어터] = 2
G1.graph[고부기][드림씨어터] = 5
G1.graph[코야코][드림씨어터] = 5

#놀거리->음식점
G1.graph[국립어린이과학관][페르시안궁전] = 6
G1.graph[국립어린이과학관][이삭토스트] = 5
G1.graph[국립어린이과학관][나누미떡볶이] = 4
G1.graph[국립어린이과학관][머노까머나] = 3
G1.graph[국립어린이과학관][뎁짜이] = 4
G1.graph[국립어린이과학관][호호식당] = 6
G1.graph[국립어린이과학관][메밀향그집] = 6
G1.graph[국립어린이과학관][정돈] = 7
G1.graph[국립어린이과학관][군자대한곱창] = 7
G1.graph[국립어린이과학관][칸다소바] = 8
G1.graph[국립어린이과학관][순대실록] = 11
G1.graph[국립어린이과학관][핏제리아오] = 14
G1.graph[국립어린이과학관][투파인드피터] = 12
G1.graph[국립어린이과학관][고부기] = 15
G1.graph[국립어린이과학관][코야코] = 15

G1.graph[짚풀박물관][페르시안궁전] = 5
G1.graph[짚풀박물관][이삭토스트] = 4
G1.graph[짚풀박물관][나누미떡볶이] = 6
G1.graph[짚풀박물관][머노까머나] = 6
G1.graph[짚풀박물관][뎁짜이] = 6
G1.graph[짚풀박물관][호호식당] = 8
G1.graph[짚풀박물관][메밀향그집] = 6
G1.graph[짚풀박물관][정돈] = 10
G1.graph[짚풀박물관][군자대한곱창] = 5
G1.graph[짚풀박물관][칸다소바] = 7
G1.graph[짚풀박물관][순대실록] = 10
G1.graph[짚풀박물관][핏제리아오] = 13
G1.graph[짚풀박물관][투파인드피터] = 12
G1.graph[짚풀박물관][고부기] = 13
G1.graph[짚풀박물관][코야코] = 14

G1.graph[아르코미술관][페르시안궁전] = 15
G1.graph[아르코미술관][이삭토스트] = 14
G1.graph[아르코미술관][나누미떡볶이] = 13
G1.graph[아르코미술관][머노까머나] = 10
G1.graph[아르코미술관][뎁짜이] = 9
G1.graph[아르코미술관][호호식당] = 7
G1.graph[아르코미술관][메밀향그집] = 7
G1.graph[아르코미술관][정돈] = 6
G1.graph[아르코미술관][군자대한곱창] = 8
G1.graph[아르코미술관][칸다소바] = 7
G1.graph[아르코미술관][순대실록] = 5
G1.graph[아르코미술관][핏제리아오] = 4
G1.graph[아르코미술관][투파인드피터] = 2
G1.graph[아르코미술관][고부기] = 3
G1.graph[아르코미술관][코야코] = 2

G1.graph[낙산공원][페르시안궁전] = 20
G1.graph[낙산공원][이삭토스트] = 19
G1.graph[낙산공원][나누미떡볶이] = 18
G1.graph[낙산공원][머노까머나] = 14
G1.graph[낙산공원][뎁짜이] = 14
G1.graph[낙산공원][호호식당] = 13
G1.graph[낙산공원][메밀향그집] = 12
G1.graph[낙산공원][정돈] = 12
G1.graph[낙산공원][군자대한곱창] = 12
G1.graph[낙산공원][칸다소바] = 11
G1.graph[낙산공원][순대실록] = 6
G1.graph[낙산공원][핏제리아오] = 6
G1.graph[낙산공원][투파인드피터] = 7
G1.graph[낙산공원][고부기] = 6
G1.graph[낙산공원][코야코] = 6

#음식점->놀거리
G1.graph[페르시안궁전][국립어린이과학관] = 6
G1.graph[이삭토스트][국립어린이과학관] = 5
G1.graph[나누미떡볶이][국립어린이과학관] = 4
G1.graph[머노까머나][국립어린이과학관] = 3
G1.graph[뎁짜이][국립어린이과학관] = 4
G1.graph[호호식당][국립어린이과학관] = 6
G1.graph[메밀향그집][국립어린이과학관] = 6
G1.graph[정돈][국립어린이과학관] = 7
G1.graph[군자대한곱창][국립어린이과학관] = 7
G1.graph[칸다소바][국립어린이과학관] = 8
G1.graph[순대실록][국립어린이과학관] = 11
G1.graph[핏제리아오][국립어린이과학관] = 14
G1.graph[투파인드피터][국립어린이과학관] = 12
G1.graph[고부기][국립어린이과학관] = 15
G1.graph[코야코][국립어린이과학관] = 15

G1.graph[페르시안궁전][짚풀박물관] = 5
G1.graph[이삭토스트][짚풀박물관] = 4
G1.graph[나누미떡볶이][짚풀박물관] = 6
G1.graph[머노까머나][짚풀박물관] = 6
G1.graph[뎁짜이][짚풀박물관] = 6
G1.graph[호호식당][짚풀박물관] = 8
G1.graph[메밀향그집][짚풀박물관] = 6
G1.graph[정돈][짚풀박물관] = 10
G1.graph[군자대한곱창][짚풀박물관] = 5
G1.graph[칸다소바][짚풀박물관] = 7
G1.graph[순대실록][짚풀박물관] = 10
G1.graph[핏제리아오][짚풀박물관] = 13
G1.graph[투파인드피터][짚풀박물관] = 12
G1.graph[고부기][짚풀박물관] = 13
G1.graph[코야코][짚풀박물관] = 14

G1.graph[페르시안궁전][아르코미술관] = 15
G1.graph[이삭토스트][아르코미술관] = 14
G1.graph[나누미떡볶이][아르코미술관] = 13
G1.graph[머노까머나][아르코미술관] = 10
G1.graph[뎁짜이][아르코미술관] = 9
G1.graph[호호식당][아르코미술관] = 7
G1.graph[메밀향그집][아르코미술관] = 7
G1.graph[정돈][아르코미술관] = 6
G1.graph[군자대한곱창][아르코미술관] = 8
G1.graph[칸다소바][아르코미술관] = 7
G1.graph[순대실록][아르코미술관] = 5
G1.graph[핏제리아오][아르코미술관] = 4
G1.graph[투파인드피터][아르코미술관] = 2
G1.graph[고부기][아르코미술관] = 3
G1.graph[코야코][아르코미술관] = 2

G1.graph[페르시안궁전][낙산공원] = 20
G1.graph[이삭토스트][낙산공원] = 19
G1.graph[나누미떡볶이][낙산공원] = 18
G1.graph[머노까머나][낙산공원] = 14
G1.graph[뎁짜이][낙산공원] = 14
G1.graph[호호식당][낙산공원] = 13
G1.graph[메밀향그집][낙산공원] = 12
G1.graph[정돈][낙산공원] = 12
G1.graph[군자대한곱창][낙산공원] = 12
G1.graph[칸다소바][낙산공원] = 11
G1.graph[순대실록][낙산공원] = 6
G1.graph[핏제리아오][낙산공원] = 6
G1.graph[투파인드피터][낙산공원] = 7
G1.graph[고부기][낙산공원] = 6
G1.graph[코야코][낙산공원] = 6

#놀거리->연극
G1.graph[국립어린이과학관][링크아트센터] = 11
G1.graph[국립어린이과학관][서연아트홀] = 6
G1.graph[국립어린이과학관][쿼드] = 12
G1.graph[국립어린이과학관][예스24스테이지] = 11
G1.graph[국립어린이과학관][컬쳐씨어터] = 12
G1.graph[국립어린이과학관][자유극장] = 12
G1.graph[국립어린이과학관][티오엠] = 12
G1.graph[국립어린이과학관][드림씨어터] = 12

G1.graph[짚풀박물관][링크아트센터] = 9
G1.graph[짚풀박물관][서연아트홀] = 3
G1.graph[짚풀박물관][쿼드] = 10
G1.graph[짚풀박물관][예스24스테이지] = 10
G1.graph[짚풀박물관][컬쳐씨어터] = 11
G1.graph[짚풀박물관][자유극장] = 11
G1.graph[짚풀박물관][티오엠] = 11
G1.graph[짚풀박물관][드림씨어터] = 11

G1.graph[아르코미술관][링크아트센터] = 9
G1.graph[아르코미술관][서연아트홀] = 9
G1.graph[아르코미술관][쿼드] = 5
G1.graph[아르코미술관][예스24스테이지] = 4
G1.graph[아르코미술관][컬쳐씨어터] = 3
G1.graph[아르코미술관][자유극장] = 4
G1.graph[아르코미술관][티오엠] = 3
G1.graph[아르코미술관][드림씨어터] = 3

G1.graph[낙산공원][링크아트센터] = 9
G1.graph[낙산공원][서연아트홀] = 12
G1.graph[낙산공원][쿼드] = 6
G1.graph[낙산공원][예스24스테이지] = 7
G1.graph[낙산공원][컬쳐씨어터] = 6
G1.graph[낙산공원][자유극장] = 6
G1.graph[낙산공원][티오엠] = 7
G1.graph[낙산공원][드림씨어터] = 7

#연극->놀거리
G1.graph[링크아트센터][국립어린이과학관] = 11
G1.graph[서연아트홀][국립어린이과학관] = 6
G1.graph[쿼드][국립어린이과학관] = 12
G1.graph[예스24스테이지][국립어린이과학관] = 11
G1.graph[컬쳐씨어터][국립어린이과학관] = 12
G1.graph[자유극장][국립어린이과학관] = 12
G1.graph[티오엠][국립어린이과학관] = 12
G1.graph[드림씨어터][국립어린이과학관] = 12

G1.graph[링크아트센터][짚풀박물관] = 9
G1.graph[서연아트홀][짚풀박물관] = 3
G1.graph[쿼드][짚풀박물관] = 10
G1.graph[예스24스테이지][짚풀박물관] = 10
G1.graph[컬쳐씨어터][짚풀박물관] = 11
G1.graph[자유극장][짚풀박물관] = 11
G1.graph[티오엠][짚풀박물관] = 11
G1.graph[드림씨어터][짚풀박물관] = 11

G1.graph[링크아트센터][아르코미술관] = 9
G1.graph[서연아트홀][아르코미술관] = 9
G1.graph[쿼드][아르코미술관] = 5
G1.graph[예스24스테이지][아르코미술관] = 4
G1.graph[컬쳐씨어터][아르코미술관] = 3
G1.graph[자유극장][아르코미술관] = 4
G1.graph[티오엠][아르코미술관] = 3
G1.graph[드림씨어터][아르코미술관] = 3

G1.graph[링크아트센터][낙산공원] = 9
G1.graph[서연아트홀][낙산공원] = 12
G1.graph[쿼드][낙산공원] = 6
G1.graph[예스24스테이지][낙산공원] = 7
G1.graph[컬쳐씨어터][낙산공원] = 6
G1.graph[자유극장][낙산공원] = 6
G1.graph[티오엠][낙산공원] = 7
G1.graph[드림씨어터][낙산공원] = 7

print('## 장소 간 전체 연결도 ##')
printGraph(G1)



user_nodes = [혜화역, 이삭토스트, 학림, 코야코]

## 최소 시간 및 경로 계산 및 출력 부분 ##
min_cost, path = G1.getMinCostTour(user_nodes)
path_name = ' -> '.join(nameAry[i] for i in path)
print(f"주어진 노드 {', '.join(nameAry[i] for i in user_nodes)}를 방문하는 최소 비용은 {min_cost}이고, 경로는 {path_name}입니다.")
