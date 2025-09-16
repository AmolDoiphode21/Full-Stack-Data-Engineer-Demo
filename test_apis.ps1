# test_apis.ps1

$baseUrl = "http://127.0.0.1:8000/api"

# =============================
# GET All Products
# =============================
Write-Host "=== GET All Products ==="
Invoke-RestMethod -Uri "$baseUrl/products/" -Method GET | Format-Table id, name, price, description

# =============================
# CREATE New Product (POST)
# =============================
Write-Host "`n=== CREATE New Product (POST) ==="
$newProduct = @{
    name = "Dell Laptop"
    price = "60000.00"
    description = "Model XPS 13"
} | ConvertTo-Json

$createdProduct = Invoke-RestMethod -Uri "$baseUrl/products/" -Method POST -ContentType "application/json" -Body $newProduct
$lastProductId = $createdProduct.id
$createdProduct | Format-Table id, name, price, description

# =============================
# UPDATE Last Product (PUT)
# =============================
Write-Host "`n=== UPDATE Last Product (PUT) ==="
$updateData = @{
    name = "Lenovo Thinkpad"
    price = "95000.00"
    description = "Updated Model"
} | ConvertTo-Json

Invoke-RestMethod -Uri "$baseUrl/products/$lastProductId/" -Method PUT -ContentType "application/json" -Body $updateData

# =============================
# PARTIAL UPDATE Last Product (PATCH)
# =============================
Write-Host "`n=== PATCH Last Product ==="
$patchData = @{
    price = "92000.00"
} | ConvertTo-Json

Invoke-RestMethod -Uri "$baseUrl/products/$lastProductId/" -Method PATCH -ContentType "application/json" -Body $patchData

# =============================
# DELETE Last Product
# =============================
Write-Host "`n=== DELETE Last Product ==="
Invoke-RestMethod -Uri "$baseUrl/products/$lastProductId/" -Method DELETE
Write-Host "Product with ID $lastProductId deleted."

# =============================
# GET Weather for Delhi
# =============================
Write-Host "`n=== GET Weather for Delhi ==="
Invoke-RestMethod -Uri "$baseUrl/weather/?city=Delhi" -Method GET | Format-Table city, temperature_C, temperature_F, humidity, description

# =============================
# GET Product Summary Report
# =============================
Write-Host "`n=== GET Product Summary Report ==="
Invoke-RestMethod -Uri "$baseUrl/product_report/" -Method GET | Format-Table total_products, avg_price, max_price, min_price
