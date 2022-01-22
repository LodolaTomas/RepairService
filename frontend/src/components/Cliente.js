import { Image } from './Image';

export const Cliente = ({nombre,apellido,image}) => {

    return (
        <div>
            <h1>{nombre}</h1>
            <h2>{apellido}</h2>
            <Image image={image} />
        </div>
    );
}

