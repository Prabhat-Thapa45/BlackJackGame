def convert(s: str, numRows: int) -> str:
        template = list(range(numRows)) + list(range(numRows - 2, 0, -1))

        result = [''] * numRows
        for i, char in enumerate(s):
            result[template[i % len(template)]] += char
        return ''.join(result)

print(convert("PAYPALISHIRING", 3))