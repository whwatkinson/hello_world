function hello_world() {
  console.log('Hello, world!\n')
}

function myMain() {
   hello_world()
}

if (require.main === module) {
    myMain();
}
