/* Lo uso para verificar si las url del back estan correctas.*/
export const Tecnico = ({cuil , nombre, apellido, email}) => {
    return(
        <>
            <h1>{cuil}</h1>
            <h1>{nombre}</h1>
            <h1>{apellido}</h1>
            <h1>{email}</h1>
        </>
    )
}
