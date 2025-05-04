# _test.py

from streamlit.testing.v1 import AppTest

def test_streamlit_app():
    at = AppTest.from_file("app.py")  # Replace with your app filename
    at.run()

    # Check title
    assert at.title[0].value == "Power Calculator"

    # Simulate entering a number
    at.number_input[0].set_value(3).run()

    # Use markdown or text components depending on how st.write renders
    markdown_values = [m.value for m in at.markdown]

    assert "The square of 3 is: 9" in markdown_values, "Square output not found"
    assert "The cube of 3 is: 27" in markdown_values, "Cube output not found"
    assert "The fifth power of 3 is: 243" in markdown_values, "Fifth power output not found"
