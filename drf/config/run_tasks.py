from config.task import longtime_add
import time

# if __name__ == '__main__':
#     result = longtime_add.delay(1,2)
#     # 이 지점에서 작업이 완료되지 않으므로 False를 반환합니다.
#     print('Task finished? ', result.ready())
#     print('Task result: ', result.result)
#     # 10초 후 작업이 완료됩니다.
#     time.sleep(10)
#     print('Task finished? ', result.ready())
#     print('Task result: ', result.result)


if __name__ == '__main__':
    f = open("config/test.txt","wt")
    f.write('sssss')
    f.close()