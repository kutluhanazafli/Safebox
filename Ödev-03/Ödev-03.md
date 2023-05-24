Analitik SQL, veritabanı sistemlerinde kullanılan bir tekniktir ve karmaşık veri analizleri ve sorguları gerçekleştirmek için kullanılır. Analitik SQL, veri manipülasyonu, segmentasyon, sıralama, toplama ve diğer analitik işlemleri gerçekleştirmek için özel olarak tasarlanmış işlevleri ve ifadeleri içerir. Bu teknik, genellikle büyük veri kümeleri üzerinde derinlemesine analiz yapmak için kullanılır ve işletmelerin satış verilerini analiz etmek, müşteri davranışlarını anlamak, pazar trendlerini belirlemek gibi birçok alanda uygulanabilir.

Örnek:

```
SELECT product_category, SUM(sales_amount) AS total_sales, AVG(unit_price) AS average_price
FROM sales_data
WHERE order_date BETWEEN '2023-01-01' AND '2023-12-31'
GROUP BY product_category
HAVING total_sales > 100000
ORDER BY total_sales DESC;
```

Bu sorgu, "sales_data" tablosundaki satış verilerini analiz etmektedir. Sorgu, belirli bir tarih aralığındaki satışları ürün kategorilerine göre gruplandırır. Her kategori için toplam satış miktarını ve ortalama birim fiyatı hesaplar. Ardından, toplam satış miktarı 100.000 birimi aşan kategorileri filtrelemek için "HAVING" ifadesini kullanır. Son olarak, sonuçları toplam satış miktarına göre azalan şekilde sıralar. Bu sorgu, en çok satılan ürün kategorilerini belirlemek ve satış performansını analiz etmek için kullanılabilir.
