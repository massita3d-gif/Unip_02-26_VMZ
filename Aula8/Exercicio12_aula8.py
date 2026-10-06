dept_ti = {"Alice": 8000, "Bruno": 6000}
dept_mkt = {"Carla": 7000, "Bruno": 6500}
funcionarios = dept_ti.copy()
funcionarios.update(dept_mkt)
print(funcionarios)