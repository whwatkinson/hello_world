function hello_world() {
  console.log('Hello World!')
}

function myMain() {
   hello_world()
}

if (require.main === module) {
    myMain();
}
