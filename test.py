from selenium import webdriver
import time
import sys, os
import re

browser = webdriver.Chrome(executable_path=str("D:\\Translation EXE\\chromedriver.exe"))
browser.maximize_window()
browser.get('https://translate.google.com/')
# Text = """Niteliği, türü ve miktarı : </b>Tip-A Telefon ( Üst Düzey Yönetici Telefonu) 	23 adet 	Tip-B Telefon ( Orta Düzey Yönetici Telefonu) 32 adet 	Tip-C Telefon (Ofis Telefonu) 230"""
Text = """Mpkl/Jk/Sh: 30/2020 - Cadangan Memasang Lampu Awam Di Padang Awam Lorong 21, Kg. Baru Sungai Jarom, Jenjarom, Kuala Langat.<BR>
Harga Dokumen : RM 150.00<BR>
Tarikh tutup : penjualan Dokumen sebut harga adalah pada 14 JULAI 2020 (SELASA). Dokumen
  Sebutharga tidak akan dikeluarkan selepas dari waktu tersebut. Sebarang
  pertanyaan sila hubungi UNIT PEROLEHAN DAN UKUR
  BAHAN di Talian 03-31872825 sambungan 118,119 dan 167.
 
 
 

 




Kod-Kod Bidang
								
									
						
							Gred CIDB
							
								
																			(G1) KEUPAYAAN TIDAK MELEBIHI RM200,000.00
																			(G2) KEUPAYAAN TIDAK MELEBIHI RM500,000.00
																			(G3) KEUPAYAAN TIDAK MELEBIHI RM1,000,000.00"""
# Text=Text.replace('\n','~$~')

# Text=Text.replace('~$~','\n')
# Text = re.sub('\n\r+', '\n', Text)

time.sleep(2)
print('sendkey')    
# browser.execute_script("document.getElementById('source').setAttribute('value', '"+str(Text)+"')")
# time.sleep(2)
for i in browser.find_elements_by_xpath('//*[@id="source"]'):
    i.send_keys(str(Text))
    break


time.sleep(10)
sys.exit()
