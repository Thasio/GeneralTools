import StringTable

def word(n):
    if n < 1:
        return ""
    w = str(n)
    return w +"x" * (n - len(w))

if __name__ == "__main__":

    #s = 'x' * 80
      
    st = StringTable.StringTable( width = 20, indent = 3, space = 3)
    #st.text_line()
    st.text_line(word(2), word(4), word(1))
    st.text_line(word(1), word(4), word(3))
    st.text_line(word(3), word(0), word(2))
    st.text_line(word(4), word(1), word(1))
    st.text_line(word(3), word(3), word(2))
    st.text_line(word(0), word(0), word(3))

    st.draw()
