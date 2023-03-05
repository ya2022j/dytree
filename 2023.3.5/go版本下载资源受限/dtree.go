package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {

	app := gin.Default()
	// 指明html加载文件目录
	app.LoadHTMLGlob("./templates/*")
	// 映射static静态文件目录
	app.Static("dytree", "./dytree") // 当客户端通过image路径访问静态文件时，服务端从"./static"目录读取静态文件
	app.Static("static", "./static") // 当客户端通过image路径访问静态文件时，服务端从"./static"目录读取静态文件
	app.Handle("GET", "/", func(context *gin.Context) {
		context.HTML(http.StatusOK, "dtree.html", nil)
	})
	app.Run(":8888")
}

// 1. 加载 目录的json文件
//
