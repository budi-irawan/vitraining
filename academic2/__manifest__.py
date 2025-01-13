#-*- coding: utf-8 -*-

{
	"name": "Academic2",
	"version": "1.0",
	"depends": [
		"base"
	],
	"author": "Akhmad Daniel Sembiring",
	"category": "Utility",
	"website": "http://vitraining.com",
	"images": [
		"static/description/images/main_screenshot.jpg"
	],
	"price": "100",
	"license": "OPL-1",
	"currency": "USD",
	"summary": "Academic application",
	"description": "",
	"data": [
		"security/groups.xml",
		"security/ir.model.access.csv",
		"view/menu.xml",
		"view/course.xml",
		"view/user.xml",
		"view/session.xml",
		"report/course.xml",
		"report/user.xml",
		"report/session.xml"
	],
	"installable": True,
	"auto_install": False,
	"application": True
}