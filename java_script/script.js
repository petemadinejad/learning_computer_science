// im so happy because i wanna study javascript
console.log("neon");
 console.log(2+2);
 let new_var=20;
 console.log(new_var);
 let fname="ali";
 fname="reza";
 let number;
 const sex="male";
 
 let isAdmin=true;
 console.log(isAdmin)
 let isStaff=undefined
 let isnull=null
 console.log(isnull)
 console.log(isStaff)
 isAdmin="ali"
 console.log(typeof isAdmin)
 let name="mohammad"
 let age=27
 let admin=true
 let person={
    name:"mohammad",
    age:27,
    admin:true 
 }
 console.log(typeof person)
 console.log(person["admin"])
let users=["ali",'mohammad']
console.log(users)
console.log(users[2])
users[2]="zahra"
console.log(users)
function Sum(name,age){
   let calc=2+2
   console.log(calc)
   console.log("yessssssssssssssssssssssss")
   console.log("hello "+name+ "you are "+age+" years old")
   console.log(age)
}
function square(r){
   return 3.14*r**2

}
let res=Sum("parisa",30)
console.log(res)
console.log(square(5))
let x=5
let y=10
console.log(5+10)
console.log(x%=2)
console.log(x>1)

if(10){
   console.log("ok")
}
let role="admin"
switch(role){
   case "guest":
      console.log("user")
      break
   case "admin":
      console.log("admin")
      break
   default:
      console.log("unknown user")
   
}
for(let i=0;i<10;i+=2){
   console.log("accept")
   console.log(i)
}
// let i=5
// while(1){
//    console.log("yes")
//    i=i-1
// }
d=3
do{
console.log("yesssss")
}while(d>5)
const person2={"name":"parisa","age":28}

for (let key in person2){
   console.log(key)
   console.log(person2[key])
}

const colors=['red','green','blue']

for (let index in colors)
   console.log(index)