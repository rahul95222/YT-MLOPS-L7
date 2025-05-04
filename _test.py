from streamlit.testing.v1 import AppTest

def test_streamlit_app():
    at = AppTest.from_file("app.py")  # replace with your actual app filename
    at.run()

    # Check the title is rendered
    assert at.title[0].value == "Power Calculator"

    # Simulate entering the number 3
    at.number_input[0].set_value(3).run()

    # Check the calculated outputs
    assert any("The square of 3 is: 9" in el.value for el in at.write), "Square output not found"
    assert any("The cube of 3 is: 27" in el.value for el in at.write), "Cube output not found"
    assert any("The fifth power of 3 is: 243" in el.value for el in at.write), "Fifth power output not found"
