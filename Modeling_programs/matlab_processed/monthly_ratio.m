load('hair_dryer.mat','hairdryer');
%load('microwave.mat', 'microwave');
%load('pacifier.mat','pacifier');
%product_name = pacifier; product_str = 'Pacifier';
%product_name = microwave; product_str = 'Microwave';
product_name = hairdryer; product_str = 'Hairdryer';

% only use date after 2008
idx_since_2008 = find(product_name.review_date.Year>=2008);
product_name = product_name(idx_since_2008,:);

product_name_no = size(product_name,1);
stars_no = zeros(5,1);
s_1 = find(product_name.star_rating==1); s_1_ratio = length(s_1)/product_name_no
s_2 = find(product_name.star_rating==2); s_2_ratio = length(s_2)/product_name_no
s_3 = find(product_name.star_rating==3); s_3_ratio = length(s_3)/product_name_no
s_4 = find(product_name.star_rating==4); s_4_ratio = length(s_4)/product_name_no
s_5 = find(product_name.star_rating==5); s_5_ratio = length(s_5)/product_name_no
vine_no = length(find(product_name.vine=='Y' | product_name.vine=='y'));
vine_ratio = vine_no/product_name_no
verified_no = length(find(product_name.verified_purchase=='Y' | product_name.verified_purchase=='y'));
verified_ratio = verified_no/product_name_no

% do monthly stars rating statistic
monthNumber=(2015-2008+1)*12-4;
monthArray=product_name.review_date(1:monthNumber);
aveMatrix=zeros(monthNumber,5);
i = 1;
r=zeros(5,1);
ave=zeros(1,5);
s=zeros(5,1);
for y=2008: 2015
    iy=find(product_name.review_date.Year==y);
    if y==2015
        n_m=8;
    else
        n_m=12;
    end
    for m=1:n_m
        im= find(product_name.review_date.Month(iy)==m)+iy(1)-1; % index of month
        if ~isempty(im)
             for k=1:5                            
                 imk=find(product_name.star_rating(im)==k)+im(1)-1;  % index of monthly rating of k
                 ave(k)=length(imk)/length(im);            
             end
        end
        monthArray(i)=datetime(y,m,15);
        aveMatrix(i,:)=ave;
        i = i + 1;
    end
end
figure
plot(monthArray,aveMatrix)
legend('1 Star','2 Stars','3 Stars','4 Stars','5 Stars')
xlabel('Year, Month (y,m)')
ylabel('Ratio')
title([product_str, ' 2008-2015'])