println "1.- Vertx Application is done!"
vertx.deployVerticle("ping.groovy"){ ping ->
  if(ping.succeeded()){
    println "2.- Ping Verticle is ready!!"

    vertx.deployVerticle("pong.groovy"){pong ->
      if(pong.succeeded()){
        println "3.- Pong Verticle is ready!!"
        vertx.eventBus().send("com.cg.ping", [step:0, task:"Running Vertx"] )
      }
    }
  }
}
