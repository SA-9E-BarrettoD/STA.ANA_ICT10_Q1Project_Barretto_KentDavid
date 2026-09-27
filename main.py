from pyscript import document


def stock_generator(event):
    category = document.querySelector("#category").value
    product = document.querySelector("#product_name").value.strip()
    quantity = document.querySelector("#quantity").value
    output = document.querySelector("#sku_output")

    if not product or quantity == "":
        output.innerHTML = '<p class="text-danger text-center mb-0">Please enter a product name and quantity.</p>'
        return

    category_code = category[:3].upper()
    product_code = ''.join(product.split())[:3].upper()
    sku = f"{category_code}-{product_code}-{int(quantity):03d}"

    output.innerHTML = f'''
        <div class="result-box">
            <div class="text-muted">Generated Stock Code</div>
            <div class="sku-code">{sku}</div>
            <div class="small text-muted mt-2">{product} • {category} • Stock: {quantity}</div>
        </div>
    '''


def create_order(event):
    items = []
    total = 0

    for number in range(1, 6):
        checkbox = document.querySelector(f"#item{number}")
        if checkbox.checked:
            label = document.querySelector(f"label[for='item{number}']")
            name = label.textContent.strip()
            price = int(checkbox.value)
            items.append((name, price))
            total += price

    output = document.querySelector("#show")

    if not items:
        output.innerHTML = '<p class="text-muted text-center mb-0">Please select at least one item.</p>'
        return

    item_lines = "".join(
        f'<div class="d-flex justify-content-between"><span>{name}</span><span>₱{price}</span></div>'
        for name, price in items
    )

    output.innerHTML = f'''
        <div class="result-box">
            <div class="fw-bold mb-2">🧾 Order Summary</div>
            {item_lines}
            <hr class="my-2">
            <div class="d-flex justify-content-between receipt-total">
                <span>Total</span><span>₱{total}</span>
            </div>
        </div>
    '''
