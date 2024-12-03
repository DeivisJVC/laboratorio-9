use data_base1

db.Estudiantes.insertMany([
    {
    "nombre": "Juan",
    "edad": 20, 
    "ciudad": "Bogotá" 
    },
    {
    "nombre": "Ana",
    "edad":22,
    "ciudad": "Medellín"
    },
    {
    "nombre": "Luis",
    "edad": 19,
    "ciudad": "Cali"
    }  
]
)
//db.Estudiantes.find()
db.Estudiantes.find(
    {
        ciudad:{$in:"Bogota"}
    }
)