## Lopy 4
![lopy4](https://docs.pycom.io/gitbook/assets/expansion_board_3_lopy4.png)

### Reset
_เป็นการลบไฟล์ออกจาก storage_ ในกรณืที่โค้ดมีปัญหาแล้วทำงานไม่ได้
* กดปุ่ม safe boot แล้วเสียบ USB
* ที่ console พิมพ์
  ```python
  import os
  os.fsformat('/flash')
  ```

### Pybytes
[Pybyes](https://pybytes.pycom.io/) เป็นแพลตฟอร์มที่เอาไว้เชื่อมต่อกับอุปกรณ์ pycom ผ่าน wifi lora sigfox สามารถจัดการอุปกรณ์ หรือโปรเจคของเราได้  
[การลบ pybytes](https://forum.pycom.io/topic/3513/disable-pybytes/2)