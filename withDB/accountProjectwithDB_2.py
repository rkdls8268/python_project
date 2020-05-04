import pymysql
global managerPW #관리자 비밀번호

#데이터베이스 연결
conn = pymysql.connect(host='localhost', port=3306, user='root', password='1234', db='webdb', charset='utf8')
#커서 생성
curs = conn.cursor()

class Account:
    def __init__(self, accNum, name, pw, balance):
        self.accNum = accNum
        self.name = name
        self.pw = pw
        self.balance = balance

    def print_info(self):
        print("계좌번호: ", self.accNum)
        print("이름: ", self.name)
        print("잔액: ", self.balance)
        print("=====출력되었습니다.=====")

    def get_info(): #정보 확인을 위한 함수
        print("==정보를 입력해주세요==")
        accNum = input("계좌번호: ")
        #name = input("이름: ")
        pw = input("비밀번호: ")
        return accNum, pw
       
#등록된 계좌 확인 함수
def isAccount(account_list):
    #if len(account_list) == 0:
        #print("등록된 계좌가 없습니다.")
        #return False
       
    sql = "select count(id) from webdb.account_list"
    curs.execute(sql)
    data = curs.fetchall()
    if(data[0][0] == 0):
        print("등록된 계좌가 없습니다.")
        return False
    
'''def isAccount(account_list, accNum):
    if len(account_list) == 0:
            print("등록된 계좌가 없습니다.")
            return False
    for account in account_list:
        if accNum in account.accNum:
            print("이미 등록된 계좌입니다.")
            return False
        elif accNum not in account.accNum:
            print("등록되지 않은 계좌입니다.")
            return False
    return True
'''

#계좌번호 존재 여부
def isAccNum(account_list, accNum):
    try:
        sql = "select accNum from webdb.account_list"
        curs.execute(sql)
        data = curs.fetchall()
        for i, accNum_data in enumerate(data):
            if accNum == accNum_data[0]:
                return True
            else:
                #sql = "select count(id) from webdb.account_list"
                #curs.execute(sql)
                #data = curs.fetchall()
                if i == len(data) - 1:
                    print("등록된 계좌가 없습니다.")
                    return False
    except:
        print("데이터베이스 오류 발생")
                
    '''
    for i, account in enumerate(account_list):
        if account.accNum == accNum:
            return True
        else:
            if i == len(account_list)-1:
                print("등록된 계좌가 없습니다.")
                return False '''


#계좌 개설 함수
def register(account_list):
    accNum = input("계좌번호: ")

    try:
        sql = "select accNum from webdb.account_list"
        curs.execute(sql)
        data = curs.fetchall()

        for row_data in data:
            if row_data[0] == accNum:
                print("이미 등록된 계좌입니다.")
                return

        name = input("이름: ")
        pw = input("비밀번호: ")
        balance = int(input("입금액: "))

        '''
        sql = "select count(id) from webdb.account_list"
        curs.execute(sql)
        data = curs.fetchall()
        aid = data[0][0] + 1
        '''
        
        sql = "insert into webdb.account_list(accNum, name, pw, balance) values(%s, %s, %s, %s)"
        curs.execute(sql, (accNum, name, pw, balance))
        conn.commit()
        
    except:
        print("데이터베이스 에러 발생")

    '''
    for account in account_list:
        if account.accNum == accNum:
            #account_list[i]
            print("이미 등록된 계좌입니다.")
            #register(account_list)
            return
    
    name = input("이름: ")
    pw = input("비밀번호: ")
    balance = int(input("입금액: "))
    '''    
    account = Account(accNum, name, pw, balance)
    print("계좌가 개설되었습니다.")
    return account

#입금 처리 함수
def deposit(account_list):
    if isAccount(account_list) == False:
        return
    
    accNum, pw = Account.get_info() #return값 변수에 저장
    
    if isAccNum(account_list, accNum) == False:
        return 

    sql = "select accNum, name, pw, balance from webdb.account_list"
    curs.execute(sql)
    data = curs.fetchall()
    for i, row_data in enumerate(data):
        if row_data[0] == accNum and row_data[2] == pw:
            print(row_data[1], "님 환영합니다.")
            d = int(input("입금하실 금액: "))
            b = row_data[3]
            b += d
            sql = "update webdb.account_list set balance = %s where accNum = %s"
            curs.execute(sql, (b, row_data[0]))
            conn.commit()
            
            sql = "select name, balance from webdb.account_list where accNum = %s"
            curs.execute(sql, row_data[0])
            
            data1 = curs.fetchall()
            print("정상적으로 입금되었습니다.")
            #print(data1[0])
            print(data1[0][0], "님의 잔액: ", data1[0][1])
            return
        else:
            if i != len(data) - 1:
                continue
            print("정보가 일치하지 않습니다.")
            

    '''
    for i, account in enumerate(account_list):
        if account.accNum == accNum and account.pw == pw:
            print(account.name, "님 환영합니다.")
            d = int(input("입금하실 금액: "))
            account.balance += d
            print(account.name, "님의 잔액: ", account.balance)
            return
        else:
            if i != len(account_list) - 1:
                continue
            print("정보가 일치하지 않습니다.") '''


#출금 처리 함수
def withdraw(account_list):
    if isAccount(account_list) == False:
        return
    
    accNum, pw = Account.get_info() #return값 변수에 저장
    
    if isAccNum(account_list, accNum) == False:
        return

    sql = "select accNum, name, pw, balance from webdb.account_list"
    curs.execute(sql)
    data = curs.fetchall()
    for i, row_data in enumerate(data):
        if row_data[0] == accNum and row_data[2] == pw:
            print(row_data[1], "님 환영합니다.")
            print(row_data[3])
            w = int(input("출금하실 금액: "))
            if row_data[3] >= w:
                b = row_data[3]
                b -= w

                sql1 = "update webdb.account_list set balance = %s where accNum = %s"
                curs.execute(sql1, (b, row_data[0]))
                conn.commit() #데이터 수정 및 변경 등 할 때는 commit 꼭 해줄 것
            
                sql2 = "select name, balance from webdb.account_list where accNum = %s"
                curs.execute(sql2, row_data[0])
                data1 = curs.fetchall()
                print("정상적으로 출금되었습니다.")
                print(data1[0][0], "님의 잔액: ", data1[0][1])
            else:
                print("잔액이 부족합니다.")
            return
        else:
            if i != len(data) - 1:
                continue
            print("정보가 일치하지 않습니다.")
            
    '''
    for i, account in enumerate(account_list):
        if account.accNum == accNum and account.pw == pw:
            print(account.name, "님 환영합니다.")
            w = int(input("출금하실 금액: "))
            if account.balance >= w:
                account.balance -= w
                print("정상적으로 출금되었습니다.")
                print(account.name, "님의 잔액: ", account.balance)
            else:
                print("잔액이 부족합니다.")
            return
        else:
            if i != len(account_list) - 1:
                continue
            print("정보가 일치하지 않습니다.") '''
                

#잔액 확인 함수
def myAccount(account_list):
    if isAccount(account_list) == False:
        return
    
    accNum, pw = Account.get_info() #return값 변수에 저장
    
    if isAccNum(account_list, accNum) == False:
        return
    
    sql = "select accNum, name, pw, balance from webdb.account_list"
    curs.execute(sql)
    data = curs.fetchall()
    for i, row_data in enumerate(data):
        if row_data[0] == accNum and row_data[2]  == pw:
            print("-----[정보]-----")
            print("계좌번호: ", row_data[0])
            print("이름: ", row_data[1])
            print("잔액: ", row_data[3])
            return
        else:
            if i != len(data) - 1:
                continue
            print("정보가 일치하지 않습니다.")
        
    '''    
    for i,account in enumerate(account_list):
        if account.accNum == accNum and account.pw == pw:
            account.print_info()
            #print("=====출력되었습니다.=====")
            return
        else:
            if i != len(account_list) - 1:
                continue
            print("정보가 일치하지 않습니다.") '''


#전체 고객 잔액 현황(매니저만 가능)
def showEveryAccount(account_list):
    managerPw = '1234' #관리자 비밀번호
    clientPw = input("비밀번호를 입력하세요(관리자만 접근 가능합니다): ")

    if clientPw == managerPw:
        if isAccount(account_list) == False:
            return

        try:
            sql = "select id, accNum, name, balance from webdb.account_list"
            curs.execute(sql)
            rowCount = int(curs.rowcount)
            
            for r in range(0, rowCount):
                row_data = curs.fetchone()
                print("-----[정보 " , (r + 1) , "]-----")
                print("계좌번호: ", row_data[1])
                print("이름: ", row_data[2])
                print("잔액: ", row_data[3])
        except:
            print("데이터베이스 오류 발생")
      
    else:
        print("비밀번호가 일치하지 않습니다.")
        

def delete(account_list):
    if isAccount(account_list) == False:
        return
    
    accNum, pw = Account.get_info()

    if isAccNum(account_list, accNum) == False:
        return
    
    sql = "select accNum, name, pw from webdb.account_list where accNum = %s"
    curs.execute(sql, accNum)
    data = curs.fetchall()

    if accNum == data[0][0] and pw == data[0][2]:
        while True:
            print(data[0][1], "님의 계좌[", data[0][0], "]" )
            c = input("정말로 삭제하시겠습니까? (y/n)")
            if c == 'y':
                sql = "delete from webdb.account_list where accNum = %s"
                curs.execute(sql, accNum)
                conn.commit()
                print("삭제 성공")
                break
            elif c == 'n':
                break
            else:
                print("y 또는 n 입력")
    else:
        print("비밀번호가 일치하지 않습니다.")
        

def view():
    account_list = [] #Account 클래스의 객체의 정보가 들어갈 리스트
    while True:
        choose = input('1. 계좌 개설 2. 입금 3. 출금 4. 잔액 확인 5. 전체 고객 잔액 현황 6. 계좌 삭제 7. 종료')

        if choose == '1': # 계좌 개설
            a = register(account_list) #계좌 개설 함수 호출
            if (type(a) == Account):
                account_list.append(a)
        elif choose == '2': #입금
            #입금 처리 함수 호출
            deposit(account_list)
        elif choose == '3': #출금
            #출금 처리 함수 호출
            withdraw(account_list)
        elif choose == '4': #잔액 확인
            #잔액 확인 함수 호출
            myAccount(account_list)
        elif choose == '5': #전체 고객 잔액 현황
            #전체 고객 잔액 현황 함수 호출
            showEveryAccount(account_list)
        elif choose == '6': #계좌 삭제
            delete(account_list)
        elif choose == '7': #프로그램 종료
            break
        else:
            print("1~7 사이의 정수를 입력하세요")
            #continue
    
if __name__ == "__main__":   #인터프리터에서 실행시를 위한 실행문.
    view()

#데이터베이스 연결 끊기
conn.close()
