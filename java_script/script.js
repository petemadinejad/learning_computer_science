// // im so happy because i wanna study javascript
// console.log("neon");
//  console.log(2+2);
//  let new_var=20;
//  console.log(new_var);
//  let fname="ali";
//  fname="reza";
//  let number;
//  const sex="male";
 
//  let isAdmin=true;
//  console.log(isAdmin)
//  let isStaff=undefined
//  let isnull=null
//  console.log(isnull)
//  console.log(isStaff)
//  isAdmin="ali"
//  console.log(typeof isAdmin)
//  let name="mohammad"
//  let age=27
//  let admin=true
//  let person={
//     name:"mohammad",
//     age:27,
//     admin:true 
//  }
//  console.log(typeof person)
//  console.log(person["admin"])
// let users=["ali",'mohammad']
// console.log(users)
// console.log(users[2])
// users[2]="zahra"
// console.log(users)
// function Sum(name,age){
//    let calc=2+2
//    console.log(calc)
//    console.log("yessssssssssssssssssssssss")
//    console.log("hello "+name+ "you are "+age+" years old")
//    console.log(age)
// }
// function square(r){
//    return 3.14*r**2

// }
// let res=Sum("parisa",30)
// console.log(res)
// console.log(square(5))
// let x=5
// let y=10
// console.log(5+10)
// console.log(x%=2)
// console.log(x>1)

// if(10){
//    console.log("ok")
// }
// let role="admin"
// switch(role){
//    case "guest":
//       console.log("user")
//       break
//    case "admin":
//       console.log("admin")
//       break
//    default:
//       console.log("unknown user")
   
// }
// for(let i=0;i<10;i+=2){
//    console.log("accept")
//    console.log(i)
// }
// // let i=5
// // while(1){
// //    console.log("yes")
// //    i=i-1
// // }
// d=3
// do{
// console.log("yesssss")
// }while(d>5)
// const person2={"name":"parisa","age":28}

// for (let key in person2){
//    console.log(key)
//    console.log(person2[key])
// }

// const colors=['red','green','blue']

// for (let index in colors)
//    console.log(index)


function createCircle(radius,x,y){
   return { 
      radius,
      x,
      y,
      draw(){console.log("hellp obj")}
   }
}

let obj1=createCircle(5,1,1)
// let obj2=createCircle(6,1,1)
// let obj3=createCircle(7,1,1)
// console.log(obj1)
// console.log(obj2)
// console.log(obj3)
// console.log(obj1.draw())

function SampleCode(radius){
   this.radius=radius
   this.draw=function(){
      console.log('draw')
   }
}

const sample=new SampleCode(3)
console.log(sample)

obj5=SampleCode.call({},3)
console.log(obj5)



// const obj4={
//    radius:1
// }

// obj4.color="red"
// console.log(obj4)
// obj4.draw1=function(){}
// console.log(obj4)
// delete obj4.draw1
// console.log(obj4)



// console.log(sample.constructor)
// console.log(obj1.constructor)

// let x1={}
// let x2=new Object()

// console.log(x1.constructor)
// console.log(x2.constructor)


// let x="tets string"
// console.log(x.constructor)