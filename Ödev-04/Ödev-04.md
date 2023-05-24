## Stored Procedure (Saklanmış Prosedür):
Stored Procedure, bir dizi SQL ifadesini bir araya getiren ve veritabanında saklanan bir işlevdir. Bir kez oluşturulduktan sonra, tekrar tekrar kullanılabilir ve çağrılabilir. Stored Procedure'lar aşağıdaki amaçlarla kullanılır:

Veri bütünlüğünü sağlamak: Stored Procedure'lar, veri tabanında yapılan işlemlerin doğru ve tutarlı bir şekilde gerçekleştirilmesini sağlar. Örneğin, bir alım işlemi yapıldığında, stok kontrolü yapılabilir ve gerekli güncellemeler otomatik olarak gerçekleştirilebilir.

Performansı artırmak: Stored Procedure'lar, sık kullanılan işlemleri önceden derler ve bir plan oluşturarak veritabanının performansını artırır. Bu, ağ trafiğini azaltır ve sorgu çalışma süresini optimize eder.

Güvenliği sağlamak: Stored Procedure'lar, veritabanı işlemlerini denetleyerek güvenlik önlemlerini sağlar. Kullanıcıların doğrudan tablolara erişmesini engelleyerek veri güvenliğini artırır.

### Örnek Senaryo - Stored Procedure:  
Aşağıdaki örnek, bir alım işleminin gerçekleştirildiği bir stored procedure'ü temsil etmektedir:

```
CREATE PROCEDURE ProcessPurchase
    @productId INT,
    @quantity INT,
    @customerId INT
AS
BEGIN
    -- Stok kontrolü
    IF EXISTS (SELECT * FROM Inventory WHERE ProductId = @productId AND Quantity >= @quantity)
    BEGIN
        -- Alım işlemi
        INSERT INTO Orders (ProductId, Quantity, CustomerId, OrderDate)
        VALUES (@productId, @quantity, @customerId, GETDATE())

        -- Stok güncellemesi
        UPDATE Inventory SET Quantity = Quantity - @quantity WHERE ProductId = @productId

        PRINT 'Purchase processed successfully.'
    END
    ELSE
    BEGIN
        PRINT 'Insufficient stock.'
    END
END
```

Bu stored procedure, alım işlemlerini gerçekleştirir. İlk olarak, stok kontrolü yapılır ve yeterli miktarda ürün olduğu kontrol edilir. Ardından, alım işlemi kaydedilir ve stok güncellenir. Son olarak, işlem sonucu hakkında bir mesaj yazdırılır.

## Trigger (Tetikleyici):  
Trigger, belirli bir veritabanı olayı (örneğin, bir tabloya ekleme, güncelleme veya silme) gerçekleştiğinde otomatik olarak tetiklenen bir veritabanı nesnesidir. Trigger'lar aşağıdaki amaçlarla kullanılır:

Veri bütünlüğünü korumak: Trigger'lar, veri tabanında yapılan değişikliklerin belli kurallara uygun olmasını sağlar. Örneğin, bir tabloya yeni bir kayıt eklenirken, ilgili alanların geçerli değerlere sahip olduğunu kontrol edebilir.

İzleme ve loglama: Trigger'lar, veritabanı işlemlerini izlemek ve değişiklikleri kaydetmek için kullanılabilir. Bu, denetim ve güvenlik izleme amacıyla önemli olabilir.

Veri tabanı ilişkilerini yönetmek: Trigger'lar, tablo ilişkilerini otomatik olarak yönetmek için kullanılabilir. Örneğin, bir tablodaki bir kayıt silindiğinde, ilişkili tablolardaki ilgili kayıtları güncellemek için tetikleyici kullanılabilir.

### Örnek Senaryo - Trigger:  
Aşağıdaki örnek, bir müşteri kaydının silindiğinde ilişkili siparişleri ve ödemeleri silen bir trigger'ı temsil etmektedir:

```
CREATE TRIGGER DeleteCustomer
ON Customers
FOR DELETE
AS
BEGIN
    DELETE FROM Orders WHERE CustomerId IN (SELECT CustomerId FROM DELETED)
    DELETE FROM Payments WHERE CustomerId IN (SELECT CustomerId FROM DELETED)
END
```

Bu trigger, Customers tablosunda bir müşteri kaydı silindiğinde tetiklenir. İlişkili Orders ve Payments tablolarındaki ilgili kayıtları siler.

Stored Procedure'lar ve Trigger'lar, veritabanı yönetiminde önemli rol oynar. Ancak, yanlış kullanıldığında veya aşırı kullanıldığında bazı olumsuz etkilere de sahip olabilirler. Örneğin, karmaşık ve yanlış tasarlanmış stored procedure'lar performans sorunlarına neden olabilir ve trigger'lar gereksiz tetiklemelere yol açabilir. Ayrıca, stored procedure'lar ve trigger'lar düzgün bir şekilde belgelendirilmeli ve yönetilmelidir, aksi takdirde bakım ve değişiklikler zorlaşabilir.