import React, { useState, useEffect } from 'react';
import { Link, NavLink, useLocation } from 'react-router-dom';
import { Typography } from '@mui/material';
import MenuList from '@mui/material/MenuList';
import MenuItem from '@mui/material/MenuItem';
import ListItemIcon from '@mui/material/ListItemIcon';
import SearchIcon from '@mui/icons-material/Search';
import ListItemText from '@mui/material/ListItemText';
import FavoriteBorderIcon from '@mui/icons-material/FavoriteBorder';
import CalendarMonthOutlinedIcon from '@mui/icons-material/CalendarMonthOutlined';
import AccountCircleOutlinedIcon from '@mui/icons-material/AccountCircleOutlined';
import Box from '@mui/material/Box';
import SchoolOutlinedIcon from '@mui/icons-material/SchoolOutlined';
import menuLogo from '../../../assets/public/menu_logo.svg';

const Menu = ({ auth }) => {
  const menuItemStyle = {
    minHeight: '36px',
    '& .MuiTypography-root': {
      color: 'text.secondary',
    },
    '&:hover, &.active': {
      backgroundColor: 'primary.main',
      borderRadius: '5px',
      '& .MuiSvgIcon-root, & .MuiTypography-root': {
        color: 'common.white',
      },
    },
  };

  const menuItemOtherStyle = {
    backgroundColor: 'primary.main',
    borderRadius: '5px',
    '& .MuiSvgIcon-root, & .MuiTypography-root': {
      color: 'common.white',
    },
  };

  const currentUrl = useLocation();
  const [prev, setPrev] = useState('');
  const menuPath = ['search-lessons', 'favorites', 'my-lessons', 'calendar', 'profile'];

  useEffect(() => {
    menuPath.map(el => {
      if (currentUrl.pathname.includes(el)) {
        setPrev(currentUrl.pathname);
      } else if (currentUrl.pathname.includes('settings')) {
        setPrev('');
      }
      return null;
    });
  }, [currentUrl]);

  return (
    <Box sx={{ width: '100%', height: '100vh', backgroundColor: '#F5F5F5' }}>
      <MenuList
        sx={{
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'start',
          px: 2,
          pt: 2.5,
          gap: '8px',
        }}
      >
        <div style={{ textAlign: 'center', marginBottom: '10px' }}>
          <img src={menuLogo} alt="atha yoga logo" style={{ width: '103px', height: '26px' }} />
        </div>
        <MenuItem
          component={NavLink}
          to="search-lessons"
          sx={[{ ...menuItemStyle }, prev === '/search-lessons' && { ...menuItemOtherStyle }]}
        >
          <ListItemIcon>
            <SearchIcon color="disabled" fontSize="medium" />
          </ListItemIcon>
          <ListItemText
            primary={(
              <Typography
                variant="body2"
              >
                Поиск
              </Typography>
              )}
          />
        </MenuItem>
        <MenuItem
          component={NavLink}
          to="/favorites"
          sx={[{ ...menuItemStyle }, prev === '/favorites' && { ...menuItemOtherStyle }]}
        >
          <ListItemIcon>
            <FavoriteBorderIcon color="disabled" fontSize="medium" />
          </ListItemIcon>
          <ListItemText
            primary={(
              <Typography
                variant="body2"
              >
                Избранное
              </Typography>
              )}
          />
        </MenuItem>
        <MenuItem
          component={NavLink}
          to="/my-lessons"
          sx={[{ ...menuItemStyle }, prev === '/my-lessons' && { ...menuItemOtherStyle }]}
        >
          <ListItemIcon>
            <SchoolOutlinedIcon color="disabled" fontSize="medium" />
          </ListItemIcon>
          <ListItemText
            primary={(
              <Typography
                variant="body2"
              >
                Мои занятия
              </Typography>
                )}
          />
        </MenuItem>
        <MenuItem
          component={NavLink}
          to="/calendar"
          sx={[{ ...menuItemStyle }, prev === '/calendar' && { ...menuItemOtherStyle }]}
        >
          <ListItemIcon>
            <CalendarMonthOutlinedIcon color="disabled" fontSize="medium" />
          </ListItemIcon>
          <ListItemText
            primary={(
              <Typography
                variant="body2"
              >
                Календарь
              </Typography>
                )}
          />
        </MenuItem>
        <MenuItem
          component={NavLink}
          to="/profile"
          sx={[{ ...menuItemStyle }, prev === '/profile' && { ...menuItemOtherStyle }]}
        >
          <ListItemIcon>
            <AccountCircleOutlinedIcon color="disabled" fontSize="medium" />
          </ListItemIcon>
          <ListItemText
            primary={(
              <Typography
                variant="body2"
              >
                Профиль
              </Typography>
                )}
          />
        </MenuItem>
      </MenuList>
      <Typography
        component={Link}
        variant="body2"
        color="text.secondary"
        to="/"
        sx={{
          textDecoration: 'none', position: 'absolute', bottom: '50px', left: '20px',
        }}
      >
        О проекте
      </Typography>
      <Typography
        variant="body2"
        color="text.secondary"
        onClick={auth.logout}
        sx={{
          position: 'absolute', bottom: '20px', left: '20px', cursor: 'pointer',
        }}
      >
        Выход
      </Typography>
    </Box>
  );
};

export default Menu;
