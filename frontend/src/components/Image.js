export const Image = ({image}) => {
    return (
        <picture>
            <img width='100' height="100" src={'http://127.0.0.1:8000'+ image} alt="" />
        </picture>
    );
}