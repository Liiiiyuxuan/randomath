% Define the differential equation dy/dx = sin(x) * sin(y^2)
f = @(x, y) sin(x) * y^3 * sin(y^2);  % Updated function dy/dx = sin(x) * sin(y^2)

% Set the domain for the directional field
xrange = linspace(-5, 5, 20);  % 20 points from -10 to 10
yrange = linspace(-5, 5, 20);

% Create a grid of x and y values
[X, Y] = meshgrid(xrange, yrange);

% Compute the slope at each grid point
U = ones(size(X));  % Unit length for the x-component of the arrow
V = f(X, Y);        % Compute the y-component based on the differential equation

% Normalize the arrows for uniform arrow size
N = sqrt(U.^2 + V.^2);  % Magnitude of each vector
U = U ./ N;  % Normalize x-component
V = V ./ N;  % Normalize y-component

% Plot the directional field using the quiver function
quiver(X, Y, U, V, 0.5);  % Arrow scaling factor to avoid overlap
axis tight;
axis equal;
xlabel('x');
ylabel('y');
title('Directional Field for dy/dx = sin(x) * y * sin(y^2)');

% Enhance display
grid on;  % Add a grid
