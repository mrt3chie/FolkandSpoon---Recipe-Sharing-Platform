import React from "react";

const RecipeDetail = () => {
  return (
    <div className="mt-6">
      <div className="h-[350px]">
        <img
          src="https://cookiesfordays.com/wp-content/uploads/2024/01/chocolate-chip-cookie-recipe-ft.jpg"
          alt="choco"
          srcset=""
          className="object-cover h-full w-full rounded-lg"
        />
        <div className="flex items-center">
          <h1 className="text-3xl font-medium ">Chocolate Chip Cookies</h1>
          <p className="text-[16px] font-medium">by: Nithin</p>
        </div>
      </div>
    </div>
  );
};

export default RecipeDetail;
