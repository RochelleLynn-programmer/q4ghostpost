import React from "react";
import { Link } from "react-router-dom";
import "./Header.css";

function Header() {
  return (
    <div className="header_div">
      <h1>GhostPost</h1>
      <div className="links">
        <Link to="/">
          <button>HomePage</button>
        </Link>
        <Link to="/boasts">
          <button>Boasts</button>
        </Link>
        <Link to="/roasts">
          <button>Roasts</button>
        </Link>
        <Link to="/highranked">
          <button>HighRanked</button>
        </Link>

        <Link to="/newpost">
          <button>NewPost</button>
        </Link>
      </div>
    </div>
  );
}

export default Header;
