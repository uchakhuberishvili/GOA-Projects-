#შექმენით პროგრამა, სადაც მოახდენთ სიაზე მუშაობას. თქვენ გადმოგეცემათ ერთი სია, დავალება კი შემდეგია:
# უნდა დაითვალოთ ლუწ ინდექსებზე მყოფი რიცხვების ჯამი, ასევე კენტ ინდექსებზე მყოფი რიცხვების ჯამი.
#საბოლოოდ ორივე დაამატოთ ახალ სიაში და დააბრუნოთ ეს სია. გამოიყენეთ შემდეგი სიები:

n1 = [80]
n2 = [100,50]
n3 = [50,60,70,80]
n4 = [13,27,49]
n5 = [70,58,75,34,91]
n1_answer = []
n2_answer = []
for i in n1:
    if i % 2 ==0:
        n1_answer.append(i)
print(n1_answer)
for i in n2:
    if i % 2 ==0:
        n2_answer.append(i)
        
#Test cases:

#[80] -> [80,0]
#[100,50] -> [100,50]
#[50,60,70,80] -> [120,140]
#[13,27,49] -> [62,27]
#[70,58,75,34,91] -> [236,92]