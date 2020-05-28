% function for drawing a vector with arrow
function vectarrow(p0,p1)
% see also <https://www.mathworks.com/matlabcentral/fileexchange/
%        7470-plot-2d-3d-vector-with-arrow?s_tid=prof_contriblnk>
x0 = p0(1);  
y0 = p0(2);
x1 = p1(1);
y1 = p1(2);
plot([x0;x1],[y0;y1],'r');   % Draw a line between p0 and p1

p = p1-p0;
alpha = 0.1;  % Size of arrow head relative to the length of the vector
beta = 0.1;   % Width of the base of the arrow head relative to the length

hu = [x1-alpha*(p(1)+beta*(p(2)+eps)); x1; x1-alpha*(p(1)-beta*(p(2)+eps))];
hv = [y1-alpha*(p(2)-beta*(p(1)+eps)); y1; y1-alpha*(p(2)+beta*(p(1)+eps))];

hold on
plot(hu(:),hv(:),'b')  % Plot arrow head
hold off
end

