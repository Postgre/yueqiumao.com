	# -*- coding: utf-8 -*-    
	import paho.mqtt.client as mqtt  
	
	# 连接成功回调函数  
	def on_connect(client, userdata, flags, rc):  
	    print("Connected with result code " + str(rc))  
	    # 连接完成之后订阅gpio主题  
	    client.subscribe("gpio")  
	  
	# 消息推送回调函数  
	def on_message(client, userdata, msg):  
	    print(msg.topic+" "+str(msg.payload))  
	
	if __name__ == '__main__':  
	    client = mqtt.Client()  
	    client.on_connect = on_connect  
	    client.on_message = on_message  
	
	    try:  
	        # 请根据实际情况改变MQTT代理服务器的IP地址  
	        client.connect("iot.eclipse.org", 1883, 60)  
	        client.loop_forever()  
	    except KeyboardInterrupt:  
	        client.disconnect()  
	
	
	# from paho.mqtt import publish
	# publish.single("gpio", "hello", hostname="iot.eclipse.org")