import streamlit as st

st.set_page_config(
    page_title="Restaurant Bill Generator",
    page_icon="🍔",
    layout="centered"
)

st.title("🍔 Restaurant Bill Generator")
st.write("Select food items and quantities to generate your bill.")

menu = {
    "Burger": 120,
    "Pizza": 250,
    "French Fries": 90,
    "Pasta": 180,
    "Sandwich": 100,
    "Cold Drink": 60
}

st.subheader("🧾 Select Items")

selected_items = {}

for item, price in menu.items():

    col1, col2 = st.columns([3, 1])

    with col1:
        selected = st.checkbox(f"{item} — ₹{price}")

    with col2:
        quantity = st.number_input(
            "Qty",
            min_value=1,
            max_value=20,
            value=1,
            key=f"qty_{item}",
            disabled=not selected
        )

    if selected:
        selected_items[item] = {
            "price": price,
            "quantity": quantity
        }

discount = st.number_input(
    "Discount (%)",
    min_value=0.0,
    max_value=50.0,
    value=0.0,
    step=1.0
)

tax = st.number_input(
    "Tax (%)",
    min_value=0.0,
    max_value=30.0,
    value=5.0,
    step=1.0
)

if st.button("🧮 Generate Bill", use_container_width=True):

    if not selected_items:
        st.warning("Please select at least one food item.")

    else:

        subtotal = sum(
            item["price"] * item["quantity"]
            for item in selected_items.values()
        )

        discount_amount = subtotal * discount / 100

        taxable_amount = subtotal - discount_amount

        tax_amount = taxable_amount * tax / 100

        grand_total = taxable_amount + tax_amount

        st.divider()

        st.subheader("🧾 Final Bill")

        for item, details in selected_items.items():

            amount = details["price"] * details["quantity"]

            st.write(
                f"**{item}** × {details['quantity']} = ₹{amount:.2f}"
            )

        st.divider()

        st.write(f"**Subtotal:** ₹{subtotal:.2f}")

        st.write(
            f"**Discount:** -₹{discount_amount:.2f}"
        )

        st.write(
            f"**Tax:** +₹{tax_amount:.2f}"
        )

        st.success(
            f"### 💰 Grand Total: ₹{grand_total:.2f}"
        )

st.caption("Thank you for visiting! 😊")