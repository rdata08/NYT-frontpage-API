import githubIcon from "./icons/github.png"
import linkedinIcon from "./icons/linkedin.png"

const Banner = () => {
    return ( 
        <nav className="banner">
            <img src={githubIcon} alt="Github Icon"></img>
            <img src={linkedinIcon} alt="Linkedin Icon"></img>
            <h2>Developer</h2>
        </nav>
    );
}
 
export default Banner;