

jlog("Hello World")

or

Server.start(Server.http,
  { title: "Hello"
  , page: function() { <h1>Hello, web!</h1> }
  }
)