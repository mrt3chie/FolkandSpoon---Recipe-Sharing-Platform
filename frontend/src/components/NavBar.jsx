import React, { useState } from "react";
import TextField from "@mui/material/TextField";
import SearchOutlinedIcon from "@mui/icons-material/SearchOutlined";
import Button from "@mui/material/Button";

const NavBar = () => {
  const [navlogin, setNavlogin] = useState(true);

  return (
    <div className="flex justify-between">
      <div>
        <h1 className="text-xl font-bold">Folks & Spoon</h1>
        <p className="text-sm">Recipe Sharing Platform</p>
      </div>
      <div className="flex items-center">
        <TextField
          id="filled-basic"
          label="Search"
          variant="outlined"
          size="small"
        />
      </div>
      {navlogin ? (
        <div>
          <Button variant="text">My Recipes</Button>
          <Button variant="text">Profile</Button>
        </div>
      ) : (
        <div>
          <Button variant="contained">Log IN</Button>
        </div>
      )}
    </div>
  );
};

export default NavBar;
