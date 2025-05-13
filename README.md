# Sudoku Solver (Python)

Bu proje, Python kullanarak geliştirilen basit bir **Sudoku çözücü** uygulamasıdır.  
Backtracking algoritması ile 9x9'luk Sudoku tahtasını çözer.

## Özellikler

- Sudoku tahtasını terminalde yazdırır.
- Geçerli hamleleri kontrol eder.
- Backtracking algoritması ile otomatik çözüm sunar.

## Kullanım

1. `sudoku_solver.py` dosyasını çalıştır:
```bash
python sudoku_solver.py
```

2. Başlangıç ve çözülmüş Sudoku tahtası ekrana yazdırılır.

## Gerekli Bilgiler

- Boş hücreler `0` ile temsil edilir.
- Sudoku çözümü başarılı olursa tahtanın tamamlanmış hali gösterilir.

## Örnek Çıktı

```
Başlangıç Sudoku Tahtası:

5 3 . | . 7 . | . . .
6 . . | 1 9 5 | . . .
...

Çözülmüş Sudoku Tahtası:

5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
...
```

## Lisans

Bu proje tamamen eğitim amaçlıdır.
