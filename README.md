## Lopy 4
![lopy4](https://docs.pycom.io/gitbook/assets/expansion_board_3_lopy4.png)

### Reset
_เป็นการลบไฟล์ออกจาก storage_
* กดปุ่ม safe boot แล้วเสียบ USB
* ที่ console พิมพ์
  ```python
  import os
  os.fsformat('/flash')
  ```