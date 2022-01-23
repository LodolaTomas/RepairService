import { Image } from './Image.js';

export const Cliente = ({ nombre, apellido, image }) => {

    return (
        <>
            <h1>{nombre}</h1>
            <h2>{apellido}</h2>
            <Image image={image} />
        </>
    );
}

