
vertx.eventBus().consumer("com.cg.pong"){ message ->
  def pongMsg = message.body()
  pongMsg.step++
  println "Pong Consumer On: Increase Step ${pongMsg.step}"

  if(pongMsg.step < 10000){
    //If step < 10000 send the same message
    vertx.eventBus().send("com.cg.ping", pongMsg)
  }else{
    println "***************************************"
    println "Process Ended Ok"
    println "***************************************"
  }
}
