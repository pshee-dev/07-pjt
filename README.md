# [07-pjt] 도서 데이터를 제공하는 RESTful API 서버 구축


## 목표
- Django REST Framework를 활용하여 API 서버를 제작 
- HTTP request methods에 대한 이해 
- HTTP response status codes에 대한 이해 
- Many to one relationship(N:1)에 대한 이해 
- Many to many relationship(N:M)에 대한 이해


## 개발 언어 및 툴
- Python 3.11 
- Postman 
- Visual Studio Code 
  

## 준비사항
1. git clone / pull  
   ```bash
   git clone <원격저장소url>
   git pull <원격저장소url>
   ```

2. 가상환경 준비 및 라이브러리 설치
   ```bash
   python -m venv venv
   source venv/Scripts/activate
   pip install -r requirements.txt
   ```

3. 이슈 및 브랜치 생성 후 연결
   ```bash
   git switch <브랜치명>
   ```
   - main 브랜치에서 직접 작업하지 않기

4. migrate & loaddata
   ```bash
   python manage.py migrate
   python manage.py loaddata <데이터 경로1> <데이터 경로2>
   ```
   - `<데이터 경로>` → 'app폴더/fixtures/' 하위 경로 작성 <br>
   ex) `python manage.py loaddata articles/comments.json`

5. 작업 시작


## Branch Rule
```
[issueIndex]_branch_name
```
- 구현할 기능 단위로 이슈 생성 후 해당 이슈의 인덱스에 맞춰서 branch 생성 <br>
  ex) `001_CRUD_for_books`


## Commit Convention
```
[commit type]: [commit message]
```
- 커밋 메시지는 위와 같은 규칙으로 작성 <br>
  ex) `feat: 회원가입 기능 구현`

### Commit type
|구분자|내용|
|---|---|
|feat|기능 구현|
|fix|버그 수정|
|docs|문서, 주석 관련 작업|
|refactor|리팩토링|
|test|테스트 관련 작업|
|chore|기타 작업|


## PR Rule
- **Pull Request**는 반드시 팀원의 승인이 있어야 **merge** 가능
- 모든 PR은 상세한 설명과 함께 제출되어야 하며, 변경사항에 대한 이유를 명확히 기재
- merge 후에는 반드시 **팀원과 공유**하고, 공유받은 팀원은 `main` 브랜치를 최신 상태로 업데이트 후 자신의 브랜치와 병합하여 작업을 이어서 진행
- PR 승인은 팀원의 코드를 꼼꼼하게 확인 후 진행하며 필요 시 코멘트를 남겨서 원활한 소통 및 코드 리뷰 습관 기르기
  


## 실행 결과
A. category_list
   - 브라우저 접근 출력 예시
      ![alt text](/screenshot/image-3.png)

B. book_list 
   - 브라우저 접근 출력 예시 
      ![alt text](/screenshot/image-2.png)
  
C. book_detail 
   - 브라우저 접근 출력 예시
      ![alt text](/screenshot/image-1.png)

D. thread_list
   - 브라우저 접근 출력 예시
      ![alt text](/screenshot/image-4.png)

E. thread_detail 
   - 브라우저 접근 출력 예시 
      ![alt text](/screenshot/image-5.png)
   - Postman 요청 예시
     - PUT method
      ![alt text](/screenshot/image-8.png)
     - DELETE method
      ![alt text](/screenshot/image-9.png)

F. create_thread 
   - Postman 요청 예시
      ![alt text](/screenshot/image-7.png)

G. create_comment 
   - Postman 요청 예시
      ![alt text](/screenshot/image-10.png)

H. comment_detail 
   - Postman 요청 예시
     - GET method
      ![alt text](/screenshot/image-12.png)
     - PUT method
      ![alt text](/screenshot/image-11.png)
     - DELETE method
      ![alt text](/screenshot/image-6.png)


