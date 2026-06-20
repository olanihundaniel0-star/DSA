with open("open.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")
with open("file.pdf", "wb") as file:
    file.write(b"%PDF-1.4\n%âãÏÓ\n1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R >>\nendobj\n4 0 obj\n<< /Length 44 >>\nstream\nBT\n/F1 24 Tf\n100 700 Td\n(Hello, PDF!) Tj\nET\nendstream\nendobj\nxref\n0 5\n0000000000 65535 f \n0000000015 00000 n \n0000000074 00000 n \n0000000123 00000 n \n0000000196 00000 n \ntrailer\n<< /Size 5 /Root 1 0 R >>\nstartxref\n273\n%%EOF")
    