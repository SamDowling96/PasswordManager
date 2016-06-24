#!/usr/bin/env python3.4

import sqlite3

class Database_Handler:

	def __init__(self):
		conn = sqlite3.connect(sqlite_file)
		c = conn.cursor()
		
	def close_connection(self):
		conn.commit()
		conn.close()
		
	
