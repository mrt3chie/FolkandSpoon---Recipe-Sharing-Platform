import * as React from "react";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";
import CardActionArea from "@mui/material/CardActionArea";
import CardActions from "@mui/material/CardActions";

export default function ReceipeCard({ title, imgUrl, createdAt, userName }) {
  return (
    <Card sx={{ maxWidth: 345 }}>
      <CardActionArea>
        <CardMedia component="img" height="150" image={imgUrl} alt={title} />
        <CardContent>
          <Typography gutterBottom variant="h5" component="div">
            {title}
          </Typography>
          <Typography
            gutterBottom
            variant="body2"
            component="div"
            sx={{
              lineHeight: 0.5,
              fontSize: "12px",
              // Decrease line spacing
            }}
          >
            {createdAt}
          </Typography>
        </CardContent>
      </CardActionArea>
      <CardActions
        sx={{
          display: "flex", // Flexbox to align items
          justifyContent: "space-between", // Distribute space between elements
          alignItems: "center", // Vertically align center
        }}
      >
        <Button size="small" color="primary">
          Share
        </Button>

        {/* Text aligned next to the button */}
        <Typography variant="body2" color="text.secondary">
          by {userName}
        </Typography>
      </CardActions>
    </Card>
  );
}
